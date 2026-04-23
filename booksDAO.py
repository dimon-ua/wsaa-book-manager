import sqlite3

DATABASE = 'database.db'

class BooksDAO:
    def __init__(self, database=DATABASE):
        self.database = database
        
    def get_all_books(self):
        conn = sqlite3.connect(self.database)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books")        
        books = cursor.fetchall()        
        # convert Row objects to list of dicts
        books = [dict(row) for row in books]
        conn.close()
        return books

    def get_book_by_id(self, book_id):
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books WHERE id = ?", (book_id,))
        book = cursor.fetchone()
        conn.close()
        return book

booksDAO = BooksDAO()