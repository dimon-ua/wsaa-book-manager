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
    all_authors = booksDAO.get_all_authors()
    return render_template("index.html", books=books, all_authors=all_authors)


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

@app.route("/api/books", methods=["POST"])
def add_book():
    data = request.get_json()
    title = data.get("title")
    author = data.get("author")
    price = data.get("price")
    isbn = data.get("isbn")

    if not title or not author or not price or not isbn:
        return jsonify({"error": "Missing required fields"}), 400

    new_book_id = booksDAO.add_book(title, author, price, isbn)
    return jsonify({"message": "Book added successfully", "book_id": new_book_id}), 201


#------- FLASK RUNNING CODE --------
if __name__ == "__main__":
    app.run(debug=True)