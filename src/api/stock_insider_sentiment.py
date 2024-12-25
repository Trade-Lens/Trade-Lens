import finnhub
import os
import streamlit as st
from dotenv import load_dotenv
from datetime import datetime, timedelta

'''
DOCUMENTATIE API FINNHUB

Get insider sentiment data for US companies calculated using method discussed here.
- The MSPR ranges from -100 for the most negative to 100 for the most positive 
which can signal price changes in the coming 30-90 days.

- Returns:
    data = Array of sentiment data.
    change = Net buying/selling from all insiders' transactions.
    month = Month.
    mspr = Monthly share purchase ratio.
    symbol = Symbol.
    year = Year.
    symbol = Symbol of the company.

'''

@st.cache_data
def get_insider_sentiment(stock):
    load_dotenv()

    finnhub_api_key = os.getenv("FINNHUB_API_KEY")
    finnhub_client = finnhub.Client(api_key=finnhub_api_key)

    to_date = datetime.now()
    from_date = to_date - timedelta(days=365*2) # 2 ani

    to_date_str = to_date.strftime('%Y-%m-%d')
    from_date_str = from_date.strftime('%Y-%m-%d')

    # sentimentul oamenilor din companie in ultimii 2 ani
    try:
        insider_sentiment = finnhub_client.stock_insider_sentiment(stock, from_date_str, to_date_str)
        return insider_sentiment
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None
    