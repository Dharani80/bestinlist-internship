#1q
import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",password="Dharani@80")
print(mydb)
import sys
cur=ydb.cursor()
cur.execute("SELECT VERSION()")
data=cur.fetchone()
print("MYDB version:",str(data))
#2q
dbse = mydb.cursor()
dbse.execute("CREATE DATABASE MYdatabase")
dbse  = mydb.cursor()
dbse.execute("SHOW DATABASES")
for entry in dbse:
    print(entry)
mydb = mysql.connector.connect(host="localhost",user="root",password="Dharani@80")
dbse = mydb.cursor()
dbse.execute("CREATE TABLE Customers(Employee_name Varchar(255),Employee_dep varchar(255),Employee_id varchar(255))")
dbse = mydb.cursor()
dbse.execute("SHOW TABLES")
for value in dbse:
    print(value)
dbse = mydb.cursor()
dbse.execute("CREATE TABLE Office(emp_name varchar(255),Emp_ADRESS Varchar(255),emp_id int(5))")
dbse = mydb.cursor()
dbse.execute("CREATE TABLE student(rollno int(5),stud_name varchar(255),Mark int(3))")
dbse = mydb.cursor()
dbse.execute("SHOW TABLES")
for value in dbse:
    print(value)
#3q
mydb = mysql.connector.connect(host="localhost",user="root",password="Dharani@80",database="mydatabase")
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE EMPLOYEE1(id INT auto_increment PRIMARY KEY,name VARCHAR(255),address varchar(255))")     
mydb = mysql.connector.connect(host="localhost",user="root",password="Dharani@80",database = "my database")
mycursor = mydb.cursor()
sql = "INSERT INTO EMPLOYEE1(id,name,address)VALUES(%s,%s,%s)"
val = ("124","Renu","chennai")
mycursor.execute(sql,val)


mydb.commit()
print(mycursor.rowcount,"record inserted")


mycursor = mydb.cursor()
sql =  "INSERT INTO EMPLOYEE1(id,name,address)VALUES(%s,%s,%s)"
val = ("231","rani","bhagya nagar")
mycursor.execute(sql,val)

mydb.commit()
print(mycursor.rowcount,"record inserted")

mycursor = mydb.cursor()
sql = "INSERT INTO EMPLOYEE1(id,name,address)VALUES(%s,%s,%s)"
val = [
    ('1','rani','street2'),
    ('2','julee','kanai'),
    ('3','geetha','punjab'),
    ('4','sai','goa'),
    ('5','dharani','japan'),
mycursor.executemany(sql,val)

mydb.commit()
print(mycursor.rowcount,"was inserted")
mycursor = mydb.cursor()
mycursor.execute("SELECT*FROM EMPLOYEE1")
myresult = mycursor.fetchall()

for x in myresult:
    print(x)
mycursor = mydb.cursor()
mycursor.execute("SELECT NAME FROM EMPLOYEE1")
myresult = mycursor.fetchall()

for x in myresult:
    print(x)
