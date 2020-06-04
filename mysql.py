import os
import datetime
import pymysql

connection = pymysql.connect(host='localhost',
                             db='Chinook')

try:
    # Run a query
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM Friends WHERE name = 'Bob';")
        connection.commit()
finally:
    connection.close()
