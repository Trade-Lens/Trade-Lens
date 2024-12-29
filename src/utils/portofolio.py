import sqlite3
from utils.db_sql import get_connection
from auth.auth_service import get_user_id
from typing import Optional, Dict

# functie care returneaza portofoliul unui user
def get_user_portofolio(user_id: Optional[int]) -> Dict[str, Dict[str, int]]:
    if user_id is None:
        return {}
    
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT stock_symbol, shares FROM portfolios WHERE user_id = ?", (user_id,))
        rows = cursor.fetchall()
        
        # returnam un dictionar cu stock-urile si numarul de actiuni detinute
        portfolio = {row["stock_symbol"]: {row["shares"]} for row in rows}
        return portfolio
    
    finally:
        conn.close()

# functie care adauga un stock in portofoliu
def add_stock_to_portfolio(user_id: int, stock_symbol: str, quantity: float):
    conn = get_connection()
    try:
        cursor = conn.cursor()

        cursor.execute("SELECT shares FROM portfolios WHERE user_id = ? AND stock_symbol = ?", (user_id, stock_symbol))
        result = cursor.fetchone()

        # marim numarul de actiuni daca stock-ul exista deja in portofoliu
        if result:
            new_shares = quantity + result["shares"]
            cursor.execute("UPDATE portfolios SET shares = ? WHERE user_id = ? AND stock_symbol = ?", 
                           (new_shares, user_id, stock_symbol))
        else:
            cursor.execute("INSERT INTO portfolios (user_id, stock_symbol, shares) VALUES (?, ?, ?)", 
                           (user_id, stock_symbol, quantity))

        conn.commit()
    except Exception as e:
        print(f"Error updating portfolio: {e}")
    finally:
        conn.close()

# functie care sterge un stock din portofoliu
def delete_stock_from_portfolio(user_id: int, stock_symbol: str, quantity: float):
    conn = get_connection()
    try:
        cursor = conn.cursor()

        cursor.execute("SELECT shares FROM portfolios WHERE user_id = ? AND stock_symbol = ?", (user_id, stock_symbol))
        result = cursor.fetchone()

        # stergem stock-ul din portofoliu daca numarul de actiuni devine 0
        if result:
            new_shares = result["shares"] - quantity
            if new_shares > 0:
                cursor.execute("UPDATE portfolios SET shares = ? WHERE user_id = ? AND stock_symbol = ?", 
                               (new_shares, user_id, stock_symbol))
            else:
                cursor.execute("DELETE FROM portfolios WHERE user_id = ? AND stock_symbol = ?", (user_id, stock_symbol))

        conn.commit()
    except Exception as e:
        print(f"Error deleting stock from portfolio: {e}")
    finally:
        conn.close()