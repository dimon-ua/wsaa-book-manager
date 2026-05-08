from flask import Flask, render_template
from booksDAO import booksDAO
import mysql.connector
from config import config
from flask import jsonify, request


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
    

@app.route("/api/books/<int:id>", methods=["GET"])
def get_book_api(id):
    book = booksDAO.get_book_by_id(id)
    if book:
        return jsonify(book)
    else:
        return jsonify({"error": "Book not found"}), 404


#------- FLASK RUNNING CODE --------
if __name__ == "__main__":
    app.run(debug=True)