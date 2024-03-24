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
    cur.execute('''SELECT * FROM states
                   WHERE name LIKE BINARY '{}' ORDER BY id'''.format(args[4]))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
