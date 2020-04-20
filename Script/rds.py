import mysql.connector
from mysql.connector import Error

#input connector here - once running on ec2 configure IAM w/ login
#or just go direct? seems unsafe
try:
    connection = mysql.connector.connect(host='hostname',
                                         database='***',
                                         user='***',
                                         password='***')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to RDS", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to RDS", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("RDS connection is closed")