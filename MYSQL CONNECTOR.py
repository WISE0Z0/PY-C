#MYSQL CONNECTOR WITH PYCHARM---
import mysql.connector
conn = mysql.connector.connect(host = "localhost",database = "EMP",user = "root",password = "9440693257@Gdk")
cursor = conn.cursor()
print(conn.is_connected())

#GETTING DATA FROM A TABLE--[LIST]--
mysql = "select * from Emp_data"
cursor.execute(mysql)
rows = cursor.fetchall()
print(rows)

#TO GET DATA IN ROWS INSTEAD OF LIST--
mysql = "select * from Emp_data"
cursor.execute(mysql)
rows = cursor.fetchall()
for data in rows:
    print(data)


