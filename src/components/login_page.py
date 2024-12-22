import streamlit as st
from auth.auth_service import login_user, register_user
from components.styles.landing_page_styles import landing_page_styles

def show_login_page():
    st.markdown(landing_page_styles(), unsafe_allow_html=True)
    st.title("Welcome to Trade-Lens")
    st.text("The best place to manage your stock portfolio. Please login or register to continue.")
    
    tabs = st.tabs(["Login", "Register"])
    
    # Login
    with tabs[0]:
        st.subheader("Login")
        login_username = st.text_input("Username", key="login_username")
        login_password = st.text_input("Password", type="password", key="login_password")
        if st.button("Login"):
            if login_user(login_username, login_password):
                st.success("Login successful!")
                st.session_state["logged_in_user"] = login_username
                st.session_state["page"] = "main"
                st.rerun()
            else:
                st.error("Invalid credentials.")
            
    # Register
    with tabs[1]:
        st.subheader("Register")
        register_username = st.text_input("New Username", key="register_username")
        register_password = st.text_input("New Password", type="password", key="register_password")
        if st.button("Register"):
            if register_user(register_username, register_password):
                st.success("User registered successfully!")
            else:
                st.error("Registration failed. Username might exist.")