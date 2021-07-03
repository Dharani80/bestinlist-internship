#1
import mysql.connector
mydb=mysql.connector.connect(host ="localhost",use="root",posword="dharani@80")
print(mydb)
dbse=mydb.cursor()
dbse,execute("CREATE DSTSBASE Doctor s1")
dbse=mydb.cursor()
dbse.excute("SHOW DATABASES")
for entry in dbse:
    print(entry)

dbse.excute("CREAT TABLE Doctors(dr_id Varchar(233).patients_ visited Varchar(233))")
dbse.execute("SHOW TABLE")  
for value in dbse:
    print(value)

dbse=mydb.cursor()
sql="INSERT INTO Doctors*(dr_id,patients_visited)values(%s,%s)"
val=[('DID1','10'),('DID2','3'),('DID3','8'),('DID5','4'),('DID67','9'),('DID8','40'),('DID56','5')]
dbse.executemany(sql,val)
mydb.commit()
print(dbse.rowcount,"was inserted")
#2q
mycursor = mydb.cursor()
cursor.excute("SELECT * FROM Doctors where patient_visited >5")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

#3q
mycursor = mydb.cursor()                             
mycursor.execute("SELECT * FROM Doctors where patients_visited=0")
myresult=mycursor.fetchall()
for x in myresult:
    print(x)                         
