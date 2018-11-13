import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",passwd="",database="hackathondb")

qry = mydb.cursor()

qry.execute("SHOW TABLES")
for x in qry:
  print(x)