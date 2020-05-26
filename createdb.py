#!/usr/bin/env python3
# createdb.py
# 2020-05-24
import sqlite3

dbname = 'index.db'
conn = sqlite3.connect(dbname)
c = conn.cursor()
try:
    ddl = '''
    CREATE TABLE list
     (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        word TEXT NOT NULL,
        page INTEGER NOT NULL,
        remark TEXT
    );
     '''
    c.execute(ddl)
except sqlite3.Error as e:
    print('sqlite3.Error occurred:', e.args[0])
    
conn.commit()
conn.close()

