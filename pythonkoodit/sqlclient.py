import mysql.connector
import pymysql
pymysql.install_as_MySQLdb()
import os
import MySQLdb

import login

aUSERNAME = login.USERNAME
aPASSWORD = login.PASSWORD
aHOST= login.HOST
aDATABASE = login.DATABASE



db = mysql.connector.connect(user=aUSERNAME,password=aPASSWORD,
                             host=aHOST,database=aDATABASE)



# get cursor object
cursor= db.cursor()
# execute your query
cursor.execute("SELECT * FROM rawdata WHERE groupid=81")

# fetch all the matching rows 
result = cursor.fetchall()

# loop through the rows
for row in result:
    print(row)
    print("\n")


db.close()