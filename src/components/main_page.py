import streamlit as st
from components.sidebar import sidebar

def main_page():
    sidebar()
    
    if st.session_state.page == "main":
        # pagina principala
        st.title("Search for a specific stock:")

        col1, col2 = st.columns([3, 1])
        with col1:
            stock_query = st.text_input(
                label="Stock Symbol (invisible)",
                label_visibility="collapsed",
                placeholder="e.g. AAPL",
                key="search_input",
            )
        with col2:
            search_button = st.button("Search", key="search_button")

        # demo cu ce ar trb sa se intample (de lucrat la el)
        if st.session_state.search_button:
            st.write(f"Showing stock performance for {stock_query}")
            st.write("Stock performance:")
            st.line_chart({"AAPL": [1, 2, 6, 4, 5, 4, 5, 8, 7, 10]})

    elif st.session_state.page == "portofolio":
        # pagina de portofoliu
        st.title("My Portofolio")


