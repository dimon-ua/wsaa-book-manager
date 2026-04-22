import sqlite3

db=sqlite3.connect('database.db')

con = db.cursor()

con.execute('''CREATE TABLE IF NOT EXISTS books (
        id integer AUTO_INCREMENT PRIMARY KEY,
        title text,
        author text,
        isbn text,
        price REAL
        )
        ''')

books_list = [
    ('The Great Gatsby', 'F. Scott Fitzgerald', '978-0743273565', 12.50),
    ('To Kill a Mockingbird', 'Harper Lee', '978-0061120084', 10.99),
    ('1984', 'George Orwell', '978-0451524935', 8.50)
]

# https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.executemany
con.executemany("INSERT INTO books (title, author, isbn, price) VALUES (?, ?, ?, ?)", books_list)

# commit() method for uploading our db after creating its structure
db.commit()

db.close()