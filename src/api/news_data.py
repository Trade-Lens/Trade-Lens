import finnhub
import os
import streamlit as st
from dotenv import load_dotenv

@st.cache_data
def get_news():
    load_dotenv()

    finnhub_api_key = os.getenv("FINNHUB_API_KEY")
    finnhub_client = finnhub.Client(api_key=finnhub_api_key)

    news = finnhub_client.general_news("general", min_id=0)

    return news