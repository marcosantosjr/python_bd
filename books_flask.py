from flask import Flask, request, jsonify
import sqlite3

# Initialize Flask app
app = Flask(__name__)
DATABASE = "books.db"

# Function to connect to the database
def connect_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Create books table
def init_db():
    with connect_db() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                genre TEXT NOT NULL,
                rating REAL NOT NULL
            )
        ''')
        conn.commit()

# Initialize the database
init_db()

# Routes
@app.route('/books', methods=['GET'])
def get_books():
    with connect_db() as conn:
        books = conn.execute("SELECT * FROM books").fetchall()
        return jsonify([dict(book) for book in books])

@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    with connect_db() as conn:
        conn.execute(
            "INSERT INTO books (title, author, genre, rating) VALUES (?, ?, ?, ?)",
            (data["title"], data["author"], data["genre"], data["rating"])
        )
        conn.commit()
    return jsonify({"message": "Book added successfully"}), 201

@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    data = request.get_json()
    with connect_db() as conn:
        conn.execute(
            "UPDATE books SET title = ?, author = ?, genre = ?, rating = ? WHERE id = ?",
            (data["title"], data["author"], data["genre"], data["rating"], id)
        )
        conn.commit()
    return jsonify({"message": "Book updated successfully"})

@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    with connect_db() as conn:
        conn.execute("DELETE FROM books WHERE id = ?", (id,))
        conn.commit()
    return jsonify({"message": "Book deleted successfully"})

# Run the app
if __name__ == "__main__":
    app.run(debug=True)