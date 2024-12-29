import streamlit as st
import sqlite3
from utils.db_sql import get_connection
from auth.models import UserModel

# actualizam datele userului in baza de date
def update_user_profile(user_id, new_username, new_password):

    DB_PATH = "/home/alin/Desktop/Trade-Lens/src/utils/trade_lens.db"
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    new_password = UserModel.hash_password(new_password)
    cursor.execute(
        """
        UPDATE users
        SET username = ?, hashed_password = ?
        WHERE id = ?
        """,
        (new_username, new_password, user_id)
    )
    conn.commit()
    conn.close()