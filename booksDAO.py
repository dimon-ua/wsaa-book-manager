import mysql.connector
from config import config

DATABASE = 'database.db'

class BooksDAO:    
    def get_connection(self):
        return mysql.connector.connect(**config)
        
    def get_all_books(self):
        db = self.get_connection()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM books")
        result = cursor.fetchall()
        cursor.close()
        db.close()
        return result

    def get_book_by_id(self, book_id):
        db = self.get_connection()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM books WHERE id = %s", (book_id,))
        book = cursor.fetchone()
        cursor.close()
        db.close()
        return book
        
    def  delete_book(self, book_id):
        db = self.get_connection()
        cursor = db.cursor()
        cursor.execute("DELETE FROM books WHERE id = %s", (book_id,))
        db.commit()
        cursor.close()
        db.close()

booksDAO = BooksDAO()