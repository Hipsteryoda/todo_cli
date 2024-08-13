import sqlite3, os, yaml
from actionManager.config import source_config

conf = source_config()
DB_FILE_PATH = os.environ["HOME"] + conf['config']['db_file_path']
QUERIES_PATH = os.environ["HOME"] + conf['config']['queries_path']
queries = yaml.safe_load(open(QUERIES_PATH))

def init():
    db = sqlite3.connect(DB_FILE_PATH)
    execute(db, queries['queries']['initialize_table'])  
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

