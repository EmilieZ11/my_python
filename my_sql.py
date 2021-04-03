import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="fulcrum_1",
    password="1234"
)

print(mydb)
