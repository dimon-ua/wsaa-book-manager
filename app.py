from flask import Flask, render_template
from booksDAO import booksDAO
import mysql.connector
from config import config


app = Flask(__name__)


#------- ROUTES --------
@app.route("/")
@app.route("/index")
def index():
    books = booksDAO.get_all_books()
    return render_template("index.html", books=books)
   

@app.route("/auth")
def auth():
    return render_template("auth.html")


#------- FLASK RUNNING CODE --------
if __name__ == "__main__":
    app.run(debug=True)