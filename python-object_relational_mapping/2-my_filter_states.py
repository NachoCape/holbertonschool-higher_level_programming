#!/usr/bin/python3
"""
    takes in an argument and displays all values in the states table
    of hbtn_0e_0_usa where name matches the argument
"""
from MySQLdb import connect
import sys


if __name__ == "__main__":
    _user = sys.argv[1]
    _pass = sys.argv[2]
    _db = sys.argv[3]
    _name_state = sys.argv[4]

    db = connect(host="localhost", port=3306, user=_user,
                 password=_pass, db=_db)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE states.name='{}'\
            ORDER BY states.id ASC".format(_name_state))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
