import pandas as pd

def engineer_features(historical_df):

    # calculam schimbarea de procent a pretului si volatilitatea
    historical_df["pct_change"] = historical_df["Close"].pct_change()
    historical_df["volatility"] = historical_df["Close"].rolling(window=7).std()

    # lagurile reprezinta pretul de inchidere de acum x zile (x = 1, 7, 14, 30)
    for lag in [1, 7, 14, 30]:
        historical_df[f"lag_{lag}"] = historical_df["Close"].shift(lag)

    # calculam media si deviatia standard pt 7 si 30 de zile
    historical_df["rolling_mean_7"] = historical_df["Close"].rolling(window=7).mean()
    historical_df["rolling_std_30"] = historical_df["Close"].rolling(window=30).std()

    # eliminam randurile care contin nan
    historical_df.dropna(inplace=True)

    return historical_df
