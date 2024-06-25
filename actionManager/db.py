import sqlite3
from actionManager.config import DB_FILE_PATH

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
