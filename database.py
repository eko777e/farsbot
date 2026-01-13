import sqlite3

db = sqlite3.connect("data.db", check_same_thread=False)
cur = db.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    accepted TEXT
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS sent_words (
    user_id INTEGER,
    word TEXT
)
""")

db.commit()
