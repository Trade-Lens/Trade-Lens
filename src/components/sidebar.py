import streamlit as st
from components.styles.sidebar_styles import sidebar_styles

def sidebar():
    username = st.session_state["logged_in_user"]
    st.sidebar.title(f"Welcome, {username}!")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")

    if "page" not in st.session_state:
        st.session_state["page"] = "main"

    if st.sidebar.button("Search Stocks", use_container_width=True):
        st.session_state["page"] = "main"
        st.rerun()

    if st.sidebar.button("Market News", use_container_width=True):
        st.session_state["page"] = "market_news"
        st.rerun()

    if st.sidebar.button("Portofolio", use_container_width=True):
        st.session_state["page"] = "portofolio"
        st.rerun()

    # logout button
    if st.sidebar.button("Logout", use_container_width=True, type="primary"):
        st.session_state["logged_in_user"] = None
        st.rerun()