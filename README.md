# WSAA Book Manager

A Flask-based web application for managing a book collection with MySQL database integration.

## Features

- **Book Management**: Add, view, edit, and delete books
- **REST API**: JSON API endpoints for book operations
- **Book Covers**: Automatic cover image display using OpenLibrary API
- **Author Display**: List of authors with country information
- **Responsive UI**: Bootstrap-styled interface

## Project Structure

- [`app.py`](app.py) - Main Flask application with routes and API endpoints
- [`booksDAO.py`](booksDAO.py) - Data Access Object for database operations
- [`config.py`](config.py) - Database configuration settings
- [`init_db.py`](init_db.py) - Database initialization script
- [`requirements.txt`](requirements.txt) - Python dependencies
- [`templates/`](templates/) - HTML templates
  - [`index.html`](templates/index.html) - Main page with book list
  - [`edit_book.html`](templates/edit_book.html) - Book editing form
  - [`auth.html`](templates/auth.html) - Authentication page
- [`static/main.css`](static/main.css) - Custom CSS styles

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/dimon-ua/wsaa-book-manager.git
   cd wsaa-book-manager
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   
   > **Important:** The `mysql-connector-python` package is required. If not included automatically, install it separately:
   > ```bash
   > pip install mysql-connector-python
   > ```

3. **Set up MySQL database**:
   - Create a MySQL database named `wsaa_db`
   - Update [`config.py`](config.py) with your MySQL credentials
   - Run the database initialization:
     ```bash
     python init_db.py
     ```

## Usage

1. **Start the application**:
   ```bash
   python app.py
   ```

2. **Open your browser** and navigate to `http://localhost:5000`

3. **Log in** with the following credentials:
   - **Username:** `Andrew`
   - **Password:** `Beatty`
   
   > The login system is case-insensitive and uses `.capitalize()` for flexible authentication.

4. **Manage books** through the web interface:
   - View all books with cover images
   - Add new books via the form
   - Edit existing books
   - Delete books via the API

## Testing the API

The application uses ISBN to fetch book covers automatically from OpenLibrary API. Here are some test books to quickly validate the API:

| Title | ISBN |
|-------|------|
| Learning Python | 1565924649 |
| The Panda's Thumb | 0393300234 |
| HTML 5 | 9350040956 |

Example API test:
```bash
curl -X POST http://localhost:5000/api/books \
  -H "Content-Type: application/json" \
  -d '{"title":"Learning Python","author":"Mark Lutz","price":79.99,"isbn":"1565924649"}'
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/books` | Get all books (JSON) |
| POST | `/api/books` | Add a new book |
| GET | `/api/books/<id>` | Get a specific book by ID |
| PUT | `/api/books/<id>` | Update a book |
| DELETE | `/api/books/<id>` | Delete a book |

### API Usage Examples

**Get all books**:
```bash
curl http://localhost:5000/api/books
```

**Add a book**:
```bash
curl -X POST http://localhost:5000/api/books \
  -H "Content-Type: application/json" \
  -d '{"title":"Book Title","author":"Author Name","price":29.99,"isbn":"1234567890"}'
```

## Database Schema

### Books Table
Stores information about all books in the collection.
```sql
CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    author VARCHAR(255),
    isbn VARCHAR(20),
    price DECIMAL(10, 2)
);
```

### Authors Table
Stores author information with their country of origin.
```sql
CREATE TABLE authors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    country VARCHAR(100)
);
```

## Dependencies

- **Flask 3.1.3** - Web framework for building the application
- **mysql-connector-python** - MySQL database connector for Python
- **Bootstrap 4.1.3** - CSS framework for responsive UI design
- **OpenLibrary API** - External service for book cover images
- **Requests** - HTTP library for making API calls

## References

- [Flask Documentation](https://flask.palletsprojects.com/) - Web framework used
- [MySQL Connector/Python](https://dev.mysql.com/doc/connector-python/en/) - Database connectivity
- [Bootstrap](https://getbootstrap.com/docs/4.1/) - CSS framework for UI
- [OpenLibrary Covers API](https://openlibrary.org/dev/docs/api/covers) - Book cover images
- [Flask Quickstart](https://flask.palletsprojects.com/en/stable/quickstart/) - Routing and app setup
- [Flask JSON API](https://flask.palletsprojects.com/en/stable/api/#flask.json.jsonify) - JSON response handling
- [Why Use Secret Keys in Flask Sessions](https://gemini.google.com/app/78bf2aabbd3c04f2) - Session management
- [Flask Sessions Documentation](https://runestone.academy/ns/books/published/webfundamentals/Flask/sessions.html) - Session implementation

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source. Please check the license file for details.