#!/usr/bin/python3
'''
Working on a database
'''

import MySQLdb
import sys


if __name__ == "__main__":
    args = sys.argv
    conn = MySQLdb.connect(host="localhost", port=3306, user=args[1],
                           passwd=args[2], db=args[3], charset="utf8")
    cur = conn.cursor()
    name = args[4].split(";")[0]
    name = name.strip("'\"")
    cur.execute('''SELECT cities.id, cities.name, states.name FROM cities
                   INNER JOIN states ON states.id = cities.state_id
                   WHERE states.name LIKE BINARY '{}'
                   ORDER BY cities.id ASC'''.format(name))
    query_rows = cur.fetchall()
    for i in range(0, len(query_rows)):
        if i < len(query_rows) - 1:
            print(query_rows[i][1], end=", ")
        else:
            print(query_rows[i][1], end="")
    print()
    cur.close()
    conn.close()
