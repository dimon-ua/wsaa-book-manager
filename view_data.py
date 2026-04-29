import mysql.connector
from config import config

db = mysql.connector.connect(**config)


cursor = db.cursor()
sql="select * from books where id = %s"
values = (1,)
cursor.execute(sql, values)
result = cursor.fetchall()
for x in result:
 print(x)
cursor.close()
db.close()