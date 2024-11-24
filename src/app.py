import streamlit as st
import yfinance as yf
from components.sidebar import sidebar

def main():
    sidebar()
    st.title("Trade Lens")

if __name__ == "__main__":
    main()





