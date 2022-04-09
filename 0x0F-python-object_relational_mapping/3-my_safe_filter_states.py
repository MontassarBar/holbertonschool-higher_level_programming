#!/usr/bin/python3
''' lists all states from the database hbtn_0e_0_usa
 where name matches the argument'''


import MySQLdb
from sys import argv
if __name__ == "__main__":
    db = MySQLdb.Connect(host="localhost", port=3306, user=argv[
            1], passwd=argv[2], db=argv[3])
    c = db.cursor()
    c.execute("""
        SELECT
            *
        FROM
            states
        WHERE
            name =%s
        ORDER BY id ASC
        """, (argv[4],))
    query_rows = c.fetchall()
    for row in query_rows:
        print(row)
    c.close()
    db.close()
