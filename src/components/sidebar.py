import streamlit as st
from components.styles.sidebar_styles import sidebar_styles

def sidebar():
    st.markdown(sidebar_styles(), unsafe_allow_html=True)
    username = st.session_state["logged_in_user"]
    st.sidebar.title(f"Welcome, {username}!")

    if "page" not in st.session_state:
        st.session_state["page"] = "main"

    # show the main page button
    if st.sidebar.button("Search Stocks"):
        st.session_state["page"] = "main"
        st.rerun()

    # show the portofolio button
    if st.sidebar.button("Portofolio"):
        st.session_state["page"] = "portofolio"
        st.rerun()

    # logout button
    if st.sidebar.button("Logout"):
        st.session_state["logged_in_user"] = None
        st.rerun()