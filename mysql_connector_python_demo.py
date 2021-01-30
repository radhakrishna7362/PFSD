"""
import mysql.connector

db_connection= mysql.connector.connect(host="localhost",port="3306",user="root",passwd="190031187")
print(db_connection)
"""

"""
import mysql.connector

db_connection= mysql.connector.connect(host="localhost",port="3306",user="root",passwd="190031187",auth_plugin='mysql_native_password')
print(db_connection)
"""

"""
import mysql.connector

db_connection= mysql.connector.connect(host="localhost",port="3306",user="root",passwd="190031187")
print(db_connection)
db_cursor=db_connection.cursor()
#creating database
db_cursor.execute("create database pfsd")
"""

"""
import mysql.connector

db_connection= mysql.connector.connect(host="localhost",port="3306",user="root",passwd="190031187")
print(db_connection)
db_cursor=db_connection.cursor()
#show all databases
db_cursor.execute("show databases")
for db in db_cursor:
    print(db)
"""


import mysql.connector

db_connection= mysql.connector.connect(host="localhost",port="3306",user="root",passwd="190031187",database="pfsd")
print(db_connection)
db_cursor=db_connection.cursor()

#creating tables
"""
db_cursor.execute("create table emp(id int primary key,name varchar(100))")
db_cursor.execute("create table student(id int primary key,name varchar(100))")
"""

"""
db_cursor.execute("show tables")
for table in db_cursor:
    print(table)
"""

#altering tables
"""
db_cursor.execute("alter table emp add gender varchar(100)")
"""

#inserting records
"""
db_cursor.execute("insert into emp values(1,'surya','male')")
db_connection.commit()
print(db_cursor.rowcount,"Record Inserted")

db_cursor.execute("insert into emp values(2,'klu','male')")
db_connection.commit()
print(db_cursor.rowcount,"Record Inserted")
"""

#updating records
"""
db_cursor.execute("update emp set name='klef'")
db_connection.commit()
print(db_cursor.rowcount,"Record(s) Updated")

db_cursor.execute("update emp set name='surya' where id=1")
db_connection.commit()
print(db_cursor.rowcount,"Record(s) Updated")
"""

#deleting records
"""
db_cursor.execute("delete from emp where id=1")
db_connection.commit()
print(db_cursor.rowcount,"Record(s) Deleted")
"""

#view records
"""
db_cursor.execute("select * from emp")
for row in db_cursor:
    #print(row)
    print(row[0],row[1],row[2])
"""

"""
db_cursor.execute("select count(*) from emp")
print(list(db_cursor))
print(db_cursor.fetchone()[0])
"""

"""
db_cursor.execute("select name from emp")
print(list(db_cursor))
print(db_cursor.fetchone())
print(db_cursor.fetchone()[0])
print(db_cursor.fetchall())
"""
