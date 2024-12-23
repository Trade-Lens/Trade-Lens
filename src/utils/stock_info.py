import streamlit as st
import yfinance as yf

def display_stock_info(stock_query: str) -> str:
    stock_query = stock_query.strip()
    ticker_data = yf.Ticker(stock_query)
    info = ticker_data.info

    col1, col2 = st.columns(2)

    with col1:
        # numele companiei
        st.header(info["longName"])

        st.write("")
        st.markdown(f"<span style='color:#f7df1e'>Located in: </span> {info['city']}, {info['country']}"if "city" in info and "country" in info else "N/A", unsafe_allow_html=True)
        st.markdown(f"<span style='color:#f7df1e'>Contact phone: </span> {info['phone']}" if "phone" in info else "N/A", unsafe_allow_html=True)
        st.markdown(f"<span style='color:#f7df1e'>Sector: </span> {info['sector']}" if "sector" in info else "N/A", unsafe_allow_html=True)
        st.markdown(f"<span style='color:#f7df1e'>Industry: </span> {info['industry']}" if "industry" in info else "N/A", unsafe_allow_html=True)
        st.markdown(f"<span style='color:#f7df1e'>Website: </span> <a href='{info['website']}'>{info['website']}</a>" if "website" in info else "N/A", unsafe_allow_html=True)
    with col2:
        # tabel cu informatii
        st.table({
            "Market Cap": info["marketCap"] if "marketCap" in info else "N/A",
            "Total Revenue": info["totalRevenue"] if "totalRevenue" in info else "N/A",
            "EBITDA": info["ebitda"] if "ebitda" in info else "N/A",
            "PE Ratio": info["trailingPE"] if "trailingPE" in info else "N/A",
            "EPS": info["trailingEps"] if "trailingEps" in info else "N/A",
            "Dividend Yield": info["dividendYield"] if "dividendYield" in info else "N/A",
            "Revenue Growth": info["revenueGrowth"] if "revenueGrowth" in info else "N/A",
            "Return on Assets": info["returnOnAssets"] if "returnOnAssets" in info else "N/A",
        })

        if st.button("Add to Portfolio"):
            return info["symbol"]
    