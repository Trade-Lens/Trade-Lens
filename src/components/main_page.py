import streamlit as st
from components.sidebar import sidebar
from visualization.line_area import display_line_area
from utils.stock_info import display_stock_info

def main_page():
    sidebar()

    if "viewed_stock" not in st.session_state:
        st.session_state["viewed_stock"] = None

    if st.session_state.page == "main":
        st.title("Search for a specific stock:")
        st.write("")

        col1, col2, col3 = st.columns([3, 1, 1])

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
            st.session_state["viewed_stock"] = stock_query.strip()
            st.session_state["viewed_period"] = selected_period

        elif search_button and not stock_query.strip():
            st.warning("Please enter a stock symbol before searching.")

        if st.session_state["viewed_stock"] is not None:
            display_line_area(st.session_state["viewed_stock"], 
                              period=st.session_state.get("viewed_period", "1mo"))
            display_stock_info(st.session_state["viewed_stock"])

    elif st.session_state.page == "portofolio":
        st.title("My Portfolio")

        # Ensure these exist
        if "added_stock" not in st.session_state:
            st.session_state["added_stock"] = None
        if "added_shares" not in st.session_state:
            st.session_state["added_shares"] = None

        stock = st.session_state["added_stock"]
        shares = st.session_state["added_shares"]

        if stock is not None and shares is not None:
            st.write(f"Successfully added {shares} of {stock.upper()} to your portfolio.")
            
            # resetam session state pentru stock si shares
            st.session_state["added_stock"] = None
            st.session_state["added_shares"] = None
        else:
            st.write("No newly added stock right now.")

        # demo data
        table_data = {
            "Stock Symbol": ["AAPL", "GOOGL", "AMZN"],
            "Shares": [10, 5, 15],
            "Price": [150.0, 2500.0, 3500.0],
            "Total Value": [1500.0, 12500.0, 52500.0]
        }

        st.table(table_data)
