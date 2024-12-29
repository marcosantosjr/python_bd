from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

# Initialize Flask app
app = Flask(__name__)
DATABASE = "users.db"

# Function to connect to the database
def connect_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Create users table
def init_db():
    with connect_db() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        conn.commit()

# Initialize the database
init_db()

# Routes
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data["username"]
    password = data["password"]
    hashed_password = generate_password_hash(password)

    try:
        with connect_db() as conn:
            conn.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (username, hashed_password)
            )
            conn.commit()
        return jsonify({"message": "User registered successfully"}), 201
    except sqlite3.IntegrityError:
        return jsonify({"error": "Username already exists"}), 400

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data["username"]
    password = data["password"]

    with connect_db() as conn:
        user = conn.execute(
            "SELECT * FROM users WHERE username = ?",
            (username,)
        ).fetchone()

    if user and check_password_hash(user["password"], password):
        return jsonify({"message": "Login successful!"}), 200
    else:
        return jsonify({"error": "Invalid username or password"}), 401

# Run the app
if __name__ == "__main__":
    app.run(debug=True)