#!/usr/bin/python3
"""script function that lists all states with a name"""
import MySQLdb
import sys


if __name__ == '__main__':

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], charset="utf8")
    cursor = db.cursor()
    myQuery = " ".join([
        "SELECT * FROM states",
        "WHERE name LIKE BINARY 'N%'",
        "ORDER BY id ASC"])
    cursor.execute(myQuery)
    result = cursor.fetchall()
    for rows in result:
        print(rows)
    cursor.close()
    db.close()
