import sqlite3
import hashlib

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    username TEXT,
    password TEXT
)
""")

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register(username, password):
    cursor.execute("INSERT INTO users VALUES (?, ?)",
                   (username, hash_password(password)))
    conn.commit()

def login(username, password):
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?",
                   (username, hash_password(password)))
    return cursor.fetchone()