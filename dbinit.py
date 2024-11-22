# NetWiki - CTCL 2024
# File: /dbinit.py
# Purpose: 
# Created: November 14, 2024
# Modified: November 21, 2024

from netwiki.config import loadconfig
import sys
import pymysql

print("This would delete all data, continue? [y/n]")
inp = input()
if inp != "y":
    sys.exit()

config = loadconfig()
conn = pymysql.connect(host = config.db.server, user = config.db.username, password = config.db.password, database = config.db.dbname, cursorclass = pymysql.cursors.DictCursor)
cur = conn.cursor()

with open("netwiki/db/init.sql", 'r', encoding='utf-8') as f:
    data = f.readlines()

query = ''
queries = []
for line in data:
    if not line:
        continue
    # Ignore comments
    if line.startswith('--'):
        continue
    query += line.strip() + ' '
    if ';' in query:
        queries.append(query.strip())
        query = ''

for query in queries:
    cur.execute(query)

conn.commit()