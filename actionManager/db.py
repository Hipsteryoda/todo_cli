import sqlite3, os
from actionManager.config import source_config

conf = source_config()
DB_FILE_PATH = os.environ["HOME"] + conf['config']['db_file_path']

def init():
    db = sqlite3.connect(DB_FILE_PATH)
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
    # FIXME: this is not a good way to do this
    # avoid init every time a connection is made
    init()
    return sqlite3.connect(DB_FILE_PATH)

def close(db):
    db.close()

def execute(db, query):
    db.execute(query)

def commit(db):
    db.commit()

def fetchall(db):
    return db.fetchall()

