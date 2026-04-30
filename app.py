from flask import Flask, render_template
import mysql.connector
from config import config


app = Flask(__name__)

# ------- DATABASE CONNECTION (DAO) --------
db = mysql.connector.connect(**config)


#------- ROUTES --------
@app.route("/")
@app.route("/index")
def index():
    cursor = db.cursor()
    sql="select * from books"
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    return render_template("index.html", books=result)

@app.route("/auth")
def auth():
    return render_template("auth.html")


#------- FLASK RUNNING CODE --------
if __name__ == "__main__":
    app.run(debug=True)