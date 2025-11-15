import sqlite3
from datetime import datetime

DB_NAME = "readme_history.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS readme_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            repo_url TEXT,
            generated_readme TEXT,
            created_at TEXT
        )
    """)

    conn.commit()
    conn.close()

def save_readme(repo_url, content):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("""
        INSERT INTO readme_history (repo_url, generated_readme, created_at)
        VALUES (?, ?, ?)
    """, (repo_url, content, datetime.utcnow().isoformat()))

    conn.commit()
    conn.close()

def load_history():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("SELECT id, repo_url, generated_readme, created_at FROM readme_history ORDER BY id DESC")
    rows = c.fetchall()

    conn.close()
    return rows
