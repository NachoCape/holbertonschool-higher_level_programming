#!/usr/bin/python3
# lists all states from the database hbtn_0e_0_usa:

# Your script should take 3 arguments: mysql username, mysql password and database name (no argument validation needed)
# You must use the module MySQLdb (import MySQLdb)
# Your script should connect to a MySQL server running on localhost at port 3306
# Results must be sorted in ascending order by states.id
import MySQLdb
import sys


if __name__ == "__main__":
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    arg3 = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=arg1, passwd=arg2, db=arg3)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()