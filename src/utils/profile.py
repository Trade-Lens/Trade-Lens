import streamlit as st
import sqlite3
from utils.db_sql import get_connection
from auth.models import UserModel

def update_user_profile(user_id, new_username, new_password):
    DB_PATH = "utils/trade_lens.db"
    try:
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
        st.success("User profile updated successfully!")

    except sqlite3.IntegrityError as e:
        st.error(f"Error updating profile: The username '{new_username}' might already be taken.")
        return False
    
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
        return False

    conn.close()
    return True
