#!/usr/bin/python3
"""script function to takes in arg and displays all values in MYSQL inj"""
import MySQLdb
import sys


if __name__ == '__main__':

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], charset="utf8")
    cursor = db.cursor()
    myQuery = "SELECT * FROM states WHERE name=%(name)s ORDER BY states.id"
    cursor.execute(myQuery, {'name': sys.argv[4]})
    result = cursor.fetchall()
    for rows in result:
        print(rows)
    cursor.close()
    db.close()
