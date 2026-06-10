import sqlite3

DATABASE_PATH = "database/sales.db"

def get_connection():
    return sqlite3.connect(DATABASE_PATH)