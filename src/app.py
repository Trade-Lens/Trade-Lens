import streamlit as st
from utils.db_sql import init_db
from components.login_page import show_login_page
from components.main_page import main_page

def main():
    st.set_page_config(page_title="Trade-Lens")
    init_db()

    if "logged_in_user" not in st.session_state:
        st.session_state["logged_in_user"] = None

    # prima data cand intram in aplicatie se va afisa pagina de login
    if st.session_state["logged_in_user"] is None:
        show_login_page()
    else:
        main_page()
        

if __name__ == "__main__":
    main()