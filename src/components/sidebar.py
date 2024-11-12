import streamlit as st
from components.styles.sidebar_styles import sidebar_styles

def sidebar():
    st.markdown(sidebar_styles(), unsafe_allow_html=True)
    st.sidebar.title("Welcome to Trade Lens")

    col1, col2 = st.sidebar.columns([2,2])

    login_button = col1.button("Login")
    register_button = col2.button("Register")

