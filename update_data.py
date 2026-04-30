import mysql.connector
from config import config

db = mysql.connector.connect(**config)

cursor = db.cursor()
sql="update student set name= %s, age=%s where id = %s"
values = ("Joe",33, 1)
cursor.execute(sql, values)
db.commit()
print("update done")
cursor.close()
db.close()
