import streamlit as st
import yfinance as yf
from streamlit_echarts import st_echarts

def display_line_area(stock_query: str, period: str = "1mo"):
    stock_query = stock_query.strip()
    ticker_data = yf.Ticker(stock_query)
    data = ticker_data.history(period=period)

    if data.empty:
        st.error(f"Nu exista date.")
        return

    df = data.reset_index()

    close_min = df["Close"].min() # pretul minim de inchidere
    close_max = df["Close"].max() # pretul maxim de inchidere
    ajustare_close_min = round(close_min * 0.95, 2) # 5% margin pe grafic
    ajustare_close_max = round(close_max * 1.05, 2) # 5% margin pe grafic

    x_data = df["Date"].dt.strftime("%Y-%m-%d").tolist() # datele
    y_data = df["Close"].round(2).tolist() # preturile de inchidere

    options = {
        "title": {
            "text": f"{stock_query.upper()} - {period}",
            "left": "center"
        },
        "tooltip": {
            "trigger": "axis"
        },
        "xAxis": {
            "type": "category",
            "data": x_data,
        },
        "yAxis": {
            "type": "value",
            "min": ajustare_close_min,
            "max": ajustare_close_max
        },
        "series": [
            {
                "data": y_data,
                "type": "line",
                "smooth": False,
                "showSymbol": False,
                "name": "Price:",
                "areaStyle": {}
            }
        ],
        "grid": {
            "left": "0%",
            "right": "0%",
            "top": 30,
            "bottom": 30
        }
    }

    st_echarts(options=options, height="400px", key="echarts_line_area")
