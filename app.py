import sqlite3
from flask import Flask


app = Flask(__name__)
DATABASE = 'database.db'


# ----- DATA ACCESS (DAO) -----

# https://flask.palletsprojects.com/en/stable/patterns/sqlite3/#using-sqlite-3-with-flask
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


# ----- FLASK ROUTES -----

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"



# ----- FLASK RUN SERVER ------

if __name__ == "__main__":
    app.run(debug=True)