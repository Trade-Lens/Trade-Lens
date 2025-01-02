from api.stock_insider_sentiment import get_insider_sentiment
import pandas as pd

# Pentru a determina cresterea in short term (90 de zile) vom folosi urmatoarea formula:

# adjusted_returns = predicted_returns * (1 + insider_sentiment)
# - insider_sentiment: (mspr/200) -> se normalizeaza la intervalul [-0.5, 0.5]

def adjust_returns_short(stock, predicted_returns) -> float:
    insider_sent = get_insider_sentiment(stock)

    if not insider_sent:
        return predicted_returns

    insider_sentiment = insider_sent.get("mspr", 0) / 200

    return predicted_returns * (1 + insider_sentiment)


