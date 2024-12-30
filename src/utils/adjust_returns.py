from api.analyst_recommendation import get_analyst_recommendation
from api.stock_insider_sentiment import get_insider_sentiment
from api.historical_data import fetch_historical_data
import pandas as pd

# Pentru a determina cresterea in short term (90 de zile) vom folosi urmatoarea formula:

# adjusted_returns = predicted_returns * (1 + analyst_recommendation + insider_sentiment)
# - insider_sentiment: (mspr/200) -> se normalizeaza la intervalul [-0.5, 0.5]
# - analyst_recommendation: (2 * strongBuy + buy - sell - 2 * strongSell) / total_recommendations 

# Pentru a determina cresterea in long term (180 - 365 de zile) vom face in felul urmator:
# - normalizam datele istorice (mean, std)
# - Pnou = min(max(P, medie - 2 * deviatie), medie + 2 * deviatie))


def adjust_returns_short(stock, predicted_returns) -> float:
    recomm = get_analyst_recommendation(stock)
    insider_sent = get_insider_sentiment(stock)

    if not recomm or not insider_sent:
        return predicted_returns

    recomm_df = pd.DataFrame(recomm)

    total_recomm = (
        recomm_df["buy"].sum() +
        recomm_df["sell"].sum() +
        recomm_df["strongBuy"].sum() +
        recomm_df["strongSell"].sum() +
        recomm_df["hold"].sum()
    )

    if total_recomm == 0:
        analyst_recommendation = 0
    else:
        analyst_recommendation = (
            2 * recomm_df["strongBuy"].sum() +
            recomm_df["buy"].sum() -
            recomm_df["sell"].sum() -
            2 * recomm_df["strongSell"].sum()
        ) / total_recomm

    insider_sentiment = insider_sent.get("mspr", 0) / 200

    return predicted_returns * (1 + analyst_recommendation + insider_sentiment)


def adjust_returns_long(stock , predicted_returns) -> float:
    hist_data = fetch_historical_data(stock, period='200d')

    if hist_data.empty:
        return predicted_returns
    
    mean = hist_data['Close'].mean()
    std = hist_data['Close'].std()
    
    return min(max(predicted_returns, mean - 2 * std), mean + 2 * std)

