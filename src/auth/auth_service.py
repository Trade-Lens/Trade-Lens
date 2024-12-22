from typing import Optional
from auth.models import UserModel
from utils.db_sql import get_connection

def register_user(username: str, password: str) -> bool:
    # true daca userul a fost adaugat cu succes, false altfel
    hashed_pass = UserModel.hash_password(password)
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (username, hashed_password) VALUES (?, ?)",
            (username, hashed_pass)
        )
        conn.commit()
        return True
    except Exception:
        # rollback in caz de exceptie
        conn.rollback()
        return False
    finally:
        conn.close()

def login_user(username: str, password: str) -> bool:
    # true daca userul a fost gasit si parola este corecta, false altfel
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT hashed_password FROM users WHERE username = ?", (username,))
        row = cursor.fetchone()
        if not row:
            return False
        hashed = row["hashed_password"]
        return UserModel.verify_password(password, hashed)
    finally:
        conn.close()


def get_user_id(username: str) -> Optional[int]:
    # returneaza id-ul userului daca exista, altfel None
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM users WHERE username = ?", (username,))
        row = cursor.fetchone()
        return row["id"] if row else None
    finally:
        conn.close()