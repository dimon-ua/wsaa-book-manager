from flask import Flask, render_template, redirect, url_for
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

@app.route("/add_book", methods=["POST"])
def add_book():
    title = request.form.get("title")
    author = request.form.get("author")
    price = request.form.get("price")
    isbn = request.form.get("isbn")

    new_book_id = booksDAO.add_book(title, author, price, isbn)   
   
    return redirect("/")

@app.route("/delete_book/<int:id>")
def delete_book(id):
    booksDAO.delete_book(id)
    return redirect("/")


@app.route("/edit_book/<int:book_id>")
def edit_book(book_id):
    # Fetch the book by ID
    book = booksDAO.get_book_by_id(book_id)
    return render_template("edit_book.html", book=book)
    

#------- FLASK RUNNING CODE --------
if __name__ == "__main__":
    app.run(debug=True)