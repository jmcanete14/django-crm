# Install MYSQL on computer
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python

import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = ''
)

cursorObj = database.cursor()

# create a database
cursorObj.execute("CREATE DATABASE test_db_v1")

print("All done!")