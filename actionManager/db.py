import sqlite3

def connect():
    return sqlite3.connect('actionManager/todo.db')

def close(db):
    db.close()

def execute(db, query):
    db.execute(query)

def commit(db):
    db.commit()

def fetchall(db):
    return db.fetchall()
