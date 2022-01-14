import mysql.connector

def create_connection():
    mydb = mysql.connector.connect(
      host="localhost",
      user="aicam",
      password="021021ali",
      database = "world"
    )
    print(mydb)

    return mydb