import mysql.connector
from config import config

db = mysql.connector.connect(**config)

cursor = db.cursor()

sql="update books set title= %s, price=%s where id = %s"
values = ("The Great Gatsby (Special Edition)",15.99, 1)

cursor.execute(sql, values)
db.commit()
print("update done")
cursor.close()
db.close()
