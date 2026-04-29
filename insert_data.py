import mysql.connector
from config import config

# Using ** to unpack the config dictionary and pass the values as keyword arguments to the connect() function:
db = mysql.connector.connect(**config)


cursor = db.cursor()

sql="INSERT INTO books (title, author, isbn, price) VALUES (%s, %s, %s, %s)"
values = ("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565", 10.99)

cursor.execute(sql, values)
db.commit()
print("1 record inserted, ID:", cursor.lastrowid)
cursor.close()
db.close()