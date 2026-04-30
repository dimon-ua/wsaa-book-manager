from flask import Flask, render_template
import mysql.connector
from config import config


app = Flask(__name__)

# ------- DATABASE CONNECTION (DAO) --------
db = mysql.connector.connect(**config)


#------- ROUTES --------
@app.route("/")
def index():
    cursor = db.cursor()
    sql="select * from books"
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    return render_template("index.html", books=result)



#------- FLASK RUNNING CODE --------
if __name__ == "__main__":
    app.run(debug=True)