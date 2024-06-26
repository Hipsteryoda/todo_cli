import sqlite3
from actionManager.config import DB_FILE_PATH

def init():
    db = sqlite3.connect("actionManager/todo.db")
    execute(db, """CREATE TABLE IF NOT EXISTS tasks
                (id INTEGER PRIMARY KEY AUTOINCREMENT
                , task TEXT
                , completed INTEGER
                , created_date TEXT
                , due_date TEXT
                , priority TEXT
                , completed_date TEXT
                );""")
    commit(db)
    close(db)

def connect():
    return sqlite3.connect(DB_FILE_PATH)

def close(db):
    db.close()

def execute(db, query):
    db.execute(query)

def commit(db):
    db.commit()

def fetchall(db):
    return db.fetchall()
