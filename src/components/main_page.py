import streamlit as st
import time
import pandas as pd
import yfinance as yf
from components.sidebar import sidebar
from visualization.line_area import display_line_area
from visualization.stacked_bar import display_stacked_bar
from utils.stock_info import display_stock_info
from utils.yfinance_rec import get_recommendations
from api.news_data import get_news
from api.stock_insider_sentiment import get_insider_sentiment
from api.analyst_recommendation import get_analyst_recommendation
from utils.portofolio import get_user_portofolio
from auth.auth_service import get_user_id
from utils.portofolio import delete_stock_from_portfolio

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
            search_button = st.button("Search", key="search_button", use_container_width=True)

        if search_button and stock_query.strip():
            st.session_state["viewed_stock"] = stock_query.strip()
            st.session_state["viewed_period"] = selected_period

        elif search_button and not stock_query.strip():
            st.warning("Please enter a stock symbol before searching.")

        if st.session_state["viewed_stock"] is not None:
            display_line_area(st.session_state["viewed_stock"], 
                              period=st.session_state.get("viewed_period", "1mo"))
            display_stock_info(st.session_state["viewed_stock"])
            
            st.write("")

            col1, col2 = st.columns([1.5, 1])
            with col1:
                # Recomandari analisti
                st.subheader("Analyst Recommendations")
                st.write("")

                display_stacked_bar(st.session_state["viewed_stock"])

            with col2:
                # Sentiment insideri
                st.subheader("Stock Growth Prediction")
                st.write("")
                st.write("Using our machine learning algorithms we can estimate a growth prediction based on financial strength, market sentiment, historical data, insider sentiment and other factors.")
                st.write("")

                # de implementat algoritmul de predictie cu ml 

                # recomandare yfinance
                yf_buy, yf_delta = get_recommendations(st.session_state["viewed_stock"])

                # demo vizual(datele sunt random)
                col3, col4= st.columns(2)

                with col3:
                    st.metric(label="90 days", value="+5%", delta="2%", border=True)
                    st.metric(label="365 days", value="+15%", delta="4%", border=True)

                with col4:
                    st.metric(label="180 days", value="+10%", delta="3%", border=True)
                    st.metric(label="YFINANCE RECOMMENDATION", value=yf_buy, delta=yf_delta, border=True)

                st.error("These predictions can be misleading sometimes and should not be considered financial advice.")

    elif st.session_state.page == "portofolio":
        st.title("My Portfolio")
        st.write("")

        username = st.session_state["logged_in_user"]
        user_id = get_user_id(username)
        user_portfolio = get_user_portofolio(user_id)
 
        # tabel cu portofoliul userului
        user_portfolio_df = pd.DataFrame(list(user_portfolio.items()), columns=["Stock Symbol", "Shares"])
        
        if user_portfolio_df.empty:
            st.write("Your portfolio is empty.")
            return

        for i, row in user_portfolio_df.iterrows():
            ticker_data = yf.Ticker(row["Stock Symbol"])
            info = ticker_data.info
            user_portfolio_df.at[i, "Price"] = info["previousClose"]
            user_portfolio_df.at[i, "Total Value"] = info["previousClose"] * float(list(row["Shares"])[0])
        


        col4, col5 = st.columns([5, 1.2])

        with col4:

            st.dataframe(user_portfolio_df, use_container_width=True)

        with col5:
            # dropdown cu optiuni de stergere a unui stock din portofoliu
            dropdown_options = user_portfolio_df["Stock Symbol"].tolist()

            with st.form(key="delete_stock"):
                selected_stock = st.selectbox(
                    label = "Select Stock to Delete",
                    options = dropdown_options,
                    key = "selected_stock"
                )
                delete_button = st.form_submit_button("Delete Stock", use_container_width=True)

            if delete_button:
                delete_stock_from_portfolio(user_id, selected_stock)
                st.rerun()
            
            # afisam valoarea totala a portofoliului
            cont = st.container(border=True)
            cont.write("Total Portfolio Value: " + str(user_portfolio_df["Total Value"].sum().round(2)) + " $")
        
    elif st.session_state.page == "market_news":
        st.title("Market News")
        st.write("")

        news = get_news()

        col1, col2 = st.columns(2)
        for i, article in enumerate(news[:30]):
            if i % 2 == 0:
                with col1:
                    news_container = st.container(border=True)
                    news_container.image(article["image"], use_container_width=True)
                    news_container.subheader(f"**{article['headline']}**")
                    news_container.write(article["summary"])
                    news_container.link_button("Read more", article["url"])
            else:
                with col2:
                    news_container = st.container(border=True)
                    news_container.image(article["image"], use_container_width=True)
                    news_container.subheader(f"**{article['headline']}**")
                    news_container.write(article["summary"])
                    news_container.link_button("Read more", article["url"])