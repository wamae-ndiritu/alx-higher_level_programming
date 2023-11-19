#!/usr/bin/python3
"""
List all states with name starting with N
from the database htbn_0e_0_usa
using MySQLdb
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    if len(argv) != 5:
        exit(1)

    username, password, database = argv[1], argv[2], argv[3]
    search_name = argv[4]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, password=password, db=database)

    cursor = db.cursor()

    # Execute query to receive states with the specified name
    cursor.execute("""SELECT * FROM states WHERE
                      CAST(name AS BINARY) = CAST('{}' AS BINARY)
                      ORDER BY states.id ASC""".format(search_name))

    # Fetch all the rows
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # close the cursor and db connection
    cursor.close()
    db.close()
