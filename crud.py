import mysql.connector

# connect to the database server

try:
    conn = mysql.connector.connect(
        host = '127.0.0.1',
        user = 'root',
        password = '',
        database = 'flights'
    )
    mycursor = conn.cursor()
    print('Connection established')
except:
    print('Connection Error!')

# mycursor.execute("CREATE DATABASE flights")
# conn.commit()
# data base created

# create table