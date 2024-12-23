import streamlit as st
from components.sidebar import sidebar
from visualization.line_chart import display_line_chart
from visualization.line_area import display_line_area
from utils.stock_info import display_stock_info

def main_page():
    sidebar()

    if st.session_state.page == "main":
        st.title("Search for a specific stock:")
        st.write("")

        col1, col2 , col3 = st.columns([3, 1 , 1])
        with col1:
            stock_query = st.text_input(
                label = "Stock Symbol (invisible)",
                label_visibility = "collapsed",
                placeholder = "e.g. AAPL",
                key = "search_input",
            )

        with col2:
            period_options = ["1d", "5d", "1mo", "3mo", "6mo", "1y", "max"]
            selected_period = st.selectbox(
                label = "Select Period (invisible)",
                label_visibility = "collapsed",
                options = period_options,
                index = 3 # default 3 luni
            )

        with col3:
            search_button = st.button("Search", key="search_button")

        if search_button and stock_query.strip():
            display_line_area(stock_query, period=selected_period)
            display_stock_info(stock_query)

        elif search_button and not stock_query.strip():
            st.warning("Please enter a stock symbol before searching.")
    
    elif st.session_state.page == "portofolio":
        st.title("My Portofolio")

        stock = st.session_state["added_stock"]
        shares = st.session_state["added_shares"]

        if stock is not None and shares is not None:
            st.write(f"Successfully added {shares} of {stock} to your portfolio.")
            st.session_state["added_stock"] = None
            st.session_state["added_shares"] = None
        else:
            st.write("BUG BUG BUG")

        # demo data
        table_data = {
            "Stock Symbol": ["AAPL", "GOOGL", "AMZN"],
            "Shares": [10, 5, 15],
            "Price": [150.0, 2500.0, 3500.0],
            "Total Value": [1500.0, 12500.0, 52500.0]
        }

        st.table(table_data)
