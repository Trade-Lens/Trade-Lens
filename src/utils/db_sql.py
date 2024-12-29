# src/utils/db_sql.py
import sqlite3
import os

#  in development fiecare isi schimba path-ul catre baza de date
DB_PATH = "/home/alin/Desktop/Trade-Lens/src/utils/trade_lens.db"

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    try:
        cursor = conn.cursor()
        # cream tabela 'users'
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                hashed_password TEXT NOT NULL,
                date_registered TEXT DEFAULT CURRENT_TIMESTAMP
            );
            """
        )

        # cream tabela 'portfolios' unde tinem portofoliile userilor
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS portfolios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                stock_symbol TEXT NOT NULL,
                shares REAL NOT NULL,
                FOREIGN KEY(user_id) REFERENCES users(id)
            );
            """
        )
        conn.commit()
    finally:
        conn.close()
