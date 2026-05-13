from flask import Flask, render_template, redirect, url_for, request, jsonify, session
from booksDAO import booksDAO
import requests
from flask_session import Session

# Reference: Create quick Flask app
# https://flask.palletsprojects.com/en/2.3.x/quickstart/
app = Flask(__name__)


# Reference: https://www.geeksforgeeks.org/python/how-to-use-flask-session-in-python-flask/
                    # Configuration 
app.config["SESSION_PERMANENT"] = False     # Sessions expire when the browser is closed
app.config["SESSION_TYPE"] = "filesystem"     # Store session data in files
# Reference: https://gemini.google.com/share/99748ba0b495
# we need a secret key to sign the session
app.secret_key = "my_secret_key"

# Initialize Flask-Session
Session(app)


# Login and Logout section
# Reference: https://www.geeksforgeeks.org/python/how-to-use-flask-session-in-python-flask/
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Record the user name in session
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "Andrew" and password == "Beatty":
            session["name"] = username
            return redirect(url_for("index"))
        else:
            return "Invalid login. Hint: Use your Name and Surname. Example: Andrew, Beatty."
    return render_template("login.html")

@app.route("/logout")
def logout():
    # Clear the username from session
    session["name"] = None
    return redirect(url_for("login"))



#------- ROUTES --------
# Reference: Flask routing 
# https://flask.palletsprojects.com/en/stable/quickstart/#routing
# 'index' root, main page
@app.route("/") 
def index():
    if not session.get("name"):
        return redirect(url_for("login"))
    books = booksDAO.get_all_books()
    all_authors = booksDAO.get_all_authors()
    return render_template("index.html", books=books, all_authors=all_authors)

# ****************************GET ALL***************************
# REST API route to get all books in JSON format
# Reference:  https://flask.palletsprojects.com/en/2.3.x/api/#flask.json.jsonify
# https://www.geeksforgeeks.org/python/flask-creating-rest-apis/
@app.route("/api/books", methods=["GET"])
def get_all_books_api():
    books = booksDAO.get_all_books()
    return jsonify(books)


# ****************************POST***************************
# Reference:
# https://flask.palletsprojects.com/en/stable/api/#flask.Request.get_json
@app.route("/api/books", methods=["POST"])
def add_book_api():
    data = request.get_json()
    title = data.get("title")
    author = data.get("author")
    price = data.get("price")
    isbn = data.get("isbn")

    new_book_id = booksDAO.add_book(title, author, price, isbn)
   
    return jsonify({"id": new_book_id, "message": "Book added successfully"}), 201


# ****************************PUT***************************
@app.route("/api/books/<int:book_id>", methods=["PUT"])
def update_book_api(book_id):
    data = request.get_json()
    title = data.get("title")
    author = data.get("author")
    price = data.get("price")
    isbn = data.get("isbn")

    booksDAO.update_book(book_id, title, author, price, isbn)
    
    return jsonify({"message": "Book updated successfully"})


# Route to uodate the book
@app.route("/update_book/<int:book_id>", methods=["POST"])
def update_book(book_id):
    title = request.form.get("title")
    author = request.form.get("author")
    price = request.form.get("price")
    isbn = request.form.get("isbn")
    booksDAO.update_book(book_id, title, author, price, isbn)
    return redirect("/")



# ****************************DELETE***************************
@app.route("/api/books/<int:book_id>", methods=["DELETE"])
def delete_book_api(book_id):
    booksDAO.delete_book(book_id)
    return jsonify({"message": "Book deleted successfully"})



# Route

@app.route("/api/books/<int:id>", methods=["GET"])
def get_book_api(id):
    book = booksDAO.get_book_by_id(id)
    if book:
        return jsonify(book)
    else:
        return jsonify({"error": "Book not found"}), 404

# Route to add book from HTML form
@app.route("/add_book", methods=["POST"])
def add_book():
    title = request.form.get("title")
    author = request.form.get("author")
    price = request.form.get("price")
    isbn = request.form.get("isbn")
    booksDAO.add_book(title, author, price, isbn)
    return redirect("/")


@app.route("/edit_book/<int:book_id>")
def edit_book(book_id):
    # Fetch the book by ID
    book = booksDAO.get_book_by_id(book_id)
    return render_template("edit_book.html", book=book)
    



#------- FLASK RUNNING CODE --------
if __name__ == "__main__":
    app.run(debug=True)