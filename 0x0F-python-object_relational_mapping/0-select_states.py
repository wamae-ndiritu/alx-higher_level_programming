#!/usr/bin/python3
"""
List all states from the database htbn_0e_0_usa
using MySQLdb
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    if len(argv) != 3:
        exit(1)

    username, database = argv[1], argv[2]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, password='', db=database)

    cursor = db.cursor()

    # Execute query to receive states from the database
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

    # Fetch all the rows
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # close the cursor and db connection
    cursor.close()
    db.close()
