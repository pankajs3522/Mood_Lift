import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",passwd="")

qry = mydb.cursor()

qry.execute("CREATE DATABASE hackathondb")

qry.execute("SHOW DATABASES")

for x in qry:
  print(x)