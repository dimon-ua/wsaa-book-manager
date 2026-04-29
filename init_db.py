import mysql.connector
from mysql.connector import errorcode

from config import config

# To handle connection errors, use the try statement and catch all errors using the errors.Error exception:
# https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html

try:
  cnx = mysql.connector.connect(user=config['user'],
                                password=config['password'],
                                host=config['host'],
                                database=config['database'] )
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
    cursor = cnx.cursor()
    # If no Error occurred, create the books table
    sql = """
        CREATE TABLE IF NOT EXISTS books (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255),
        author VARCHAR(255),
        isbn VARCHAR(20),
        price DECIMAL(10, 2)
    )"""
    cursor.execute(sql)
    cursor.close()
    cnx.close()