import yfinance as yf
import streamlit as st

@st.cache_data
def fetch_historical_data(ticker, period="5y"):
    stock = yf.Ticker(ticker)
    return stock.history(period=period)