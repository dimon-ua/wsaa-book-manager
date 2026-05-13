import mysql.connector
from config import config

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
        
    def delete_book(self, book_id):
        db = self.get_connection()
        cursor = db.cursor()
        cursor.execute("DELETE FROM books WHERE id = %s", (book_id,))
        db.commit()
        cursor.close()
        db.close()

    def add_book(self, title, author, price, isbn):
        db = self.get_connection()
        cursor = db.cursor()
        cursor.execute("INSERT INTO books (title, author, price, isbn) VALUES (%s, %s, %s, %s)", (title, author, price, isbn))
        db.commit()
        new_book_id = cursor.lastrowid
        cursor.close()
        db.close()
        return new_book_id

    def get_all_authors(self):
        db = self.get_connection()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM authors")
        result = cursor.fetchall()
        cursor.close()
        db.close()
        return result

    def update_book(self, book_id, title, author, price, isbn):
        db = self.get_connection()
        cursor = db.cursor()
        cursor.execute("UPDATE books SET title = %s, author = %s, price = %s, isbn = %s WHERE id = %s", (title, author, price, isbn, book_id))
        db.commit()
        cursor.close()
        db.close()

booksDAO = BooksDAO()