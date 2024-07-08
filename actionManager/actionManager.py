import os
from actionManager.db import connect, execute, commit, close
from actionManager.config import source_config
from datetime import datetime
from actionManager.bcolors import bcolors

from pomodoro.timer import Timer

try:
    conf = source_config()
    TODO_FILE_PATH = os.environ["HOME"] + conf['config']['todo_file_path']
except Exception as e:
    print(e)

def add(task, due_date=None, priority=None):
    # use sqlite3 to insert into db
    now = datetime.strftime(datetime.now(), "%Y-%m-%dT%H:%M:%S.%f") 
    db = connect()
    execute(db, f"""INSERT INTO tasks (task
                    , completed
                    , created_date
                    , due_date
                    , priority) 
                VALUES ('{task}'
                    , 0
                    , '{now}'
                    , '{due_date}'
                    , '{priority}');""")
    commit(db)
    close(db)
    syncToFile()
    list()

def collect_task_details():
    due_date = input('Due date (YYYY-MM-DD): ')
    if due_date == '':
        due_date = datetime.today().strftime("%Y-%m-%d")
    priority = input('Priority: ')
    if priority == '':
        priority = '1'
    return due_date, priority

def list():
    db = connect()
    cursor = db.cursor()
    res = cursor.execute("""SELECT id, priority, due_date, task 
                        FROM tasks
                        WHERE completed = 0
                        ORDER BY priority, due_date ASC;""")
    rows = res.fetchall()
    close(db)
    print_rows(rows)

def list_with_tag(tag):
    db = connect()
    cursor = db.cursor()
    res = cursor.execute(f"""SELECT k.id, k.priority, k.due_date, k.task 
                    FROM tasks AS k
                    left join tags as g
                    on k.id = g.task_id
                    WHERE completed = 0
                    AND tag = '{tag}'
                    ORDER BY priority, due_date ASC;""")
    rows = res.fetchall()
    close(db)
    print_rows(rows)

def print_rows(rows):
     #TODO: format headers and row values to be properly aligned
    headers = ["ID", "PRIORITY", "DUE DATE", "TASK"]
    # spacing = [10, 10, 15, 30]
    print(f"{bcolors.UNDERLINE}" + " | {: <6} | {: <15} | {: <15} | {: <30}".format(*headers) + bcolors.ENDC)
    for row in rows:
        if row[2] == datetime.strftime(datetime.now(), "%Y-%m-%d"):
            print(f"{bcolors.OKGREEN} | {row[0] : <6} | {row[1] : <15} | {row[2] : <15} | {row[3]}{bcolors.ENDC}")
        elif row[2] < datetime.strftime(datetime.now(), "%Y-%m-%d"):
            print(f"{bcolors.WARNING} | {row[0] : <6} | {row[1] : <15} | {row[2] : <15} | {row[3]}{bcolors.ENDC}")
        else:
            print(f" | {row[0] : <6} | {row[1] : <15} | {row[2] : <15} | {row[3]}")

def modify(idx):
    due_date, priority = collect_task_details()
    db = connect()
    execute(db, f"""UPDATE tasks 
                SET due_date = '{due_date}', priority = '{priority}' 
                WHERE id in ({idx});""")
    commit(db)
    close(db)
    syncToFile()
    list()

def complete(idx):
    # find the task in the database and set completed to 1
    completed_date = datetime.strftime(datetime.now(), "%Y-%m-%dT%H:%M:%S.%f")
    db = connect()
    execute(db, f"""UPDATE tasks 
                SET completed = 1, completed_date = '{completed_date}' 
                WHERE id in ({", ".join(str(i) for i in idx)});""")
    commit(db)
    close(db)
    syncToFile()
    list()

def remove(idx):
    db = connect()
    execute(db, f"""DELETE FROM tasks WHERE id in ({", ".join(str(i) for i in idx)});""")
    commit(db)
    close(db)
    syncToFile()
    list()

def tag(idx, tag):
    db = connect()
    execute(db, f"""INSERT INTO tags (task_id, tag) 
                VALUES ({idx}, '{tag}');""")
    commit(db)
    close(db)
    list_with_tag(tag)

def start_task(idx):
    # start a pomodoro timer
    db = connect()
    cursor = db.cursor()
    res = cursor.execute(f"""SELECT task
                FROM tasks
                WHERE id = {idx};""")
    task = res.fetchall()[0][0]
    close(db)
    timer = Timer(task)
    result = timer.start()
    if result == 1:
    # TODO: increment the number of pomodoros for the task
        pass

def syncFromFile():
    # TODO: read file and update db with completed tasks signified by "- [x]"
    with open(TODO_FILE_PATH, 'r') as f:
        for line in f:
            if "- [x]" in line:
                idx = line[5:].split("|")[0].strip()
                # complete(idx) <-- results in a RecursionError
                completed_date = datetime.strftime(datetime.now(), "%Y-%m-%dT%H:%M:%S.%f")
                db = connect()
                execute(db, f"""UPDATE tasks 
                            SET completed = 1, completed_date = '{completed_date}' 
                            WHERE id = {idx};""")
                commit(db)
                close(db)


def syncToFile():
    syncFromFile()
    db = connect()
    cursor = db.cursor()
    res = cursor.execute("""SELECT id, task, due_date, priority 
                        FROM tasks
                        WHERE completed = 0;""")
    rows = res.fetchall()
    close(db)
    with open(TODO_FILE_PATH, 'w') as f:
        for row in rows:
            f.write(f"- [ ] {row[0]} | {row[1]} [due:: {row[2]}] [priority:: {row[3]}]\n")

