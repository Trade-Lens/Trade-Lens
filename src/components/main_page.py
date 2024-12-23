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
            period_options = ["1d", "5d", "1wk", "1mo", "3mo", "6mo", "1y", "max"]
            selected_period = st.selectbox(
                label = "Select Period (invisible)",
                label_visibility = "collapsed",
                options = period_options,
                index = 3 # default o luna
            )

        with col3:
            search_button = st.button("Search", key="search_button")

        if search_button and stock_query.strip():
            # display_line_chart(stock_query, period=selected_period)
            display_line_area(stock_query, period=selected_period)

            add_stock = None
            add_stock = display_stock_info(stock_query)

            if add_stock:
                st.success(f"Successfully added {add_stock} to your portfolio.")

        elif search_button and not stock_query.strip():
            st.warning("Please enter a stock symbol before searching.")

    elif st.session_state.page == "portofolio":
        st.title("My Portofolio")

        # demo data
        table_data = {
            "Stock Symbol": ["AAPL", "GOOGL", "AMZN"],
            "Shares": [10, 5, 15],
            "Price": [150.0, 2500.0, 3500.0],
            "Total Value": [1500.0, 12500.0, 52500.0]
        }

        st.table(table_data)
