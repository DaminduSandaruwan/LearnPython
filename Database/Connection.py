
import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='root', passwd='',database='Damindu')
print("Connection Open")

mycursor =mydb.cursor()
mycursor.execute("show databases")

for i in mycursor:
    print(i)

mycursor.execute("select * from student")

result = mycursor.fetchall()
for i in result:
    print(i)


