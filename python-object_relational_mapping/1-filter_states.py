#!/usr/bin/python3
"""
    lists all states with a name starting with N (upper N) from
    the database hbtn_0e_0_usa:
    Your script should take 3 arguments: mysql username, mysql password and
    database name (no argument validation needed)
    You must use the module MySQLdb (import MySQLdb)
    Your script should connect to a MySQL server running on localhost
    at port 3306
    Results must be sorted in ascending order by states.id
"""
from MySQLdb import connect
import sys


if __name__ == "__main__":
    _user = sys.argv[1]
    _pass = sys.argv[2]
    _db = sys.argv[3]

    db = connect(host="localhost", port=3306, user=_user,
                 password=_pass, db=_db)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    rows = cur.fetchall()
    for row in rows:
        if row[1][0] == 'N':
            print(row)
    cur.close()
    db.close()
