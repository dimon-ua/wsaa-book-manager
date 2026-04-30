import mysql.connector
from config import config

db = mysql.connector.connect(**config)

cursor = db.cursor()
sql="delete from student where id = %s"
values = (1,)
cursor.execute(sql, values)
db.commit()
print("delete done")
cursor.close()
db.close()