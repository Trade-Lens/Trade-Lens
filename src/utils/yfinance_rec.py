import yfinance as yf

def get_recommendations(ticker):
    ticker_data = yf.Ticker(ticker)
    key = ticker_data.info["recommendationKey"] if "recommendationKey" in ticker_data.info else None
    key_delta = 0

    if key == "buy":
        key_delta = 1
        key = "Buy"
    elif key == "strong_buy":
        key_delta = 2
        key = "Strong Buy"
    elif key == "hold":
        key_delta = 0
        key = "Hold"
    elif key == "sell":
        key_delta = -1
        key = "Sell"
    elif key == "strong_sell":
        key_delta = -2
        key = "Strong Sell"

    return key, key_delta