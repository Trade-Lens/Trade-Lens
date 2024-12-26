import finnhub
import os
import streamlit as st
from dotenv import load_dotenv

@st.cache_data
def get_analyst_recommendation(stock):
    load_dotenv()

    finnhub_api_key = os.getenv("FINNHUB_API_KEY")
    finnhub_client = finnhub.Client(api_key=finnhub_api_key)

    try:
        rec = finnhub_client.recommendation_trends(stock)
    except Exception as e:
        st.error(f"An error occurred: {e}")
        rec = None

    return rec


