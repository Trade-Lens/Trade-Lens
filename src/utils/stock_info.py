import streamlit as st
import yfinance as yf
from utils.portofolio import get_user_portofolio, add_stock_to_portfolio
from auth.auth_service import get_user_id

def display_stock_info(stock_query: str):
    stock_query = stock_query.strip()
    ticker_data = yf.Ticker(stock_query)
    info = ticker_data.info

    col1, col2 = st.columns(2)

    with col1:
        with st.form(key="add_to_portfolio"):
            # numele companiei
            st.header(info["longName"])

            st.write("")
            st.markdown(f"<span style='color:#ff4b4b'>Located in: </span> {info.get('city', 'N/A')}, {info.get('country', 'N/A')}", unsafe_allow_html=True)
            st.markdown(f"<span style='color:#ff4b4b'>Contact phone: </span> {info.get('phone', 'N/A')}", unsafe_allow_html=True)
            st.markdown(f"<span style='color:#ff4b4b'>Sector: </span> {info.get('sector', 'N/A')}", unsafe_allow_html=True)
            st.markdown(f"<span style='color:#ff4b4b'>Industry: </span> {info.get('industry', 'N/A')}", unsafe_allow_html=True)
            
            st.write("")
            st.write("")
            col3, col4 , col5 = st.columns(3)

            with col3:
                st.link_button("Company Website", info["website"] if "website" in info else "#", use_container_width=True)
            
            with col4:
                shareNo = st.number_input("Shares", min_value=1.0, key="shareNo", label_visibility="collapsed", step=1.0)
    
            with col5:
                submit_button = st.form_submit_button("Add to Portfolio", use_container_width=True)
                if submit_button:
                    st.session_state["added_stock"] = info["symbol"]
                    st.session_state["added_shares"] = shareNo
                    st.session_state["added_stock_info"] = info
                    user_id = get_user_id(st.session_state["logged_in_user"])
                    add_stock_to_portfolio(user_id, info["symbol"], shareNo)
                    st.toast(f"Successfully added {shareNo} of {stock_query.upper()} to your portfolio.", icon='🎉')
            
    with col2:
        # tabel cu informatii
        st.table({
            "Market Cap": info.get("marketCap", "N/A"),
            "Total Revenue": info.get("totalRevenue", "N/A"),
            "EBITDA": info.get("ebitda", "N/A"),
            "PE Ratio": info.get("trailingPE", "N/A"),
            "PEG Ratio": info.get("pegRatio", "N/A"),
            "EPS": info.get("trailingEps", "N/A"),
            "Dividend Yield": info.get("dividendYield", "N/A"),
            "Revenue Growth": info.get("revenueGrowth", "N/A"),
            "Return on Assets": info.get("returnOnAssets", "N/A"),
            "Return on Equity": info.get("returnOnEquity", "N/A"),
        })

    with st.expander("Company description", expanded=False):
        st.write(info.get("longBusinessSummary", "N/A"))

        
    