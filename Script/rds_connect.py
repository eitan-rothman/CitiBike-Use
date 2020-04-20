import mysql.connector as mysql
from test.py import data 

mydb = mysql.connector.connect(
    host="**",
    user="**",
    passwd="***",
    database="***"
)

for mydict in data:
    placeholders = ', '.join(['%s'] * len(mydict))
    columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in mydict.keys())
    values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in mydict.values())
    sql = "INSERT INTO %s ( %s ) VALUES ( %s );" % ('mytable', columns, values)
    # print(sql)

    f = open("/home/user/files/bots.sql", "a")
    f.write(sql + '\n')


mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

