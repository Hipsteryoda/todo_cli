from config import TODO_FILE_PATH
from actionManager.db import connect, execute, commit, close, fetchall
from datetime import datetime

def add(task):
    # use sqlite3 to insert into db
    now = datetime.strftime(datetime.now(), "%Y-%m-%dT%H:%M:%S.%f") 
    db = connect()
    execute(db, f"""INSERT INTO tasks (task, completed, created_date) 
            VALUES ('{task}', 0, '{now}');""")
    commit(db)
    close(db)
    list()

def list():
    print("ID\tTASK")
    db = connect()
    cursor = db.cursor()
    res = cursor.execute("""SELECT id, task 
                        FROM tasks
                        WHERE completed = 0""")
    rows = res.fetchall()
    close(db)
    syncToFile()
    for row in rows:
        print(f"{row[0]}\t{row[1]}")

def complete(idx):
    # find the task in the database and set completed to 1
    db = connect()
    execute(db, f"UPDATE tasks SET completed = 1 WHERE id = {idx};")
    commit(db)
    close(db)
    list()

def syncToFile():
    db = connect()
    cursor = db.cursor()
    res = cursor.execute("""SELECT task 
                        FROM tasks
                        WHERE completed = 0""")
    rows = res.fetchall()
    close(db)
    with open(TODO_FILE_PATH, 'w') as f:
        for row in rows:
            f.write(f"- [ ] {row[0]}\n")
