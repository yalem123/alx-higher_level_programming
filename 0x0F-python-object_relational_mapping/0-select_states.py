#!/usr/bin/python3
"""
python script that lists all states from the database hbtn_0e_0_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states;")
    state = cursor.fetchall()

    for state in state:
        print(state)
        cursor.close()
        db.close()
