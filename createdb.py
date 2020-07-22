#!/usr/bin/env python3
# createdb.py
# 2020-05-24, 27
import sqlite3
import sys

dbname = 'index.db'
dt = datetime.today().strftime('%Y%m%d%H%M')

conn = sqlite3.connect(dbname)
c = conn.cursor()
rep = input('索引データベースを初期化します. OK?: [Y/n]')
if rep == 'N' or rep == 'No':
    sys.exit()

try:
    ddl = '''
    CREATE TABLE id
     (
        id TEXT NOT NULL
        );
    INSERT INTO id VALUES('{}');
    CREATE TABLE list
     (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        word TEXT NOT NULL,
        page INTEGER NOT NULL,
        remark TEXT
    );
     '''
    c.execute(ddl.format(dt))
except sqlite3.Error as e:
    print('sqlite3.Error occurred:', e.args[0])
    
conn.commit()
conn.close()

