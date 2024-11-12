import streamlit as st

def sidebar_styles():
    return """

    <style>

    .stButton > button {
        width: 100%;
        padding: 5px;
    }

    .stSidebar {
        display: flex;
        flex-direction: column;
        justify-content: flex-end;
        height: 100%;
    }
    </style>

    """