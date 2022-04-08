#!/usr/bin/python3
''' lists all states with a name starting with N
from the database hbtn_0e_0_usa'''


import MySQLdb
from sys import argv
if __name__ == "__main__":
    db = MySQLdb.Connect(host="localhost", port=3307, user=argv[
            1], passwd=argv[2], db=argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM states WHERE name REGEXP '^[N]' ORDER BY id ASC")
    query_rows = c.fetchall()
    for row in query_rows:
        print(row)
    c.close()
    db.close()
