from actionManager.config import TODO_FILE_PATH 
from actionManager.db import connect, execute, commit, close, init
from datetime import datetime

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

def list():
    #TODO: format headers and row values to be properly aligned
    print("ID\tDUE DATE\tPRIORITY\tTASK")
    db = connect()
    cursor = db.cursor()
    res = cursor.execute("""SELECT id, due_date, priority, task 
                        FROM tasks
                        WHERE completed = 0
                        ORDER BY priority ASC;""")
    rows = res.fetchall()
    close(db)
    for row in rows:
        print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}")

def complete(idx):
    # find the task in the database and set completed to 1
    completed_date = datetime.strftime(datetime.now(), "%Y-%m-%dT%H:%M:%S.%f")
    db = connect()
    execute(db, f"""UPDATE tasks 
                SET completed = 1, completed_date = '{completed_date}' 
                WHERE id = {idx};""")
    commit(db)
    close(db)
    syncToFile()
    list()

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

