import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from features import engineer_features
import pickle

# se ruleaza doar o singura data in development pentru a antrena modelele
def main():
    raw_data = pd.read_csv("data/historical_data.csv")
    
    features_list = []
    targets = {"90d_return": [], "180d_return": [], "365d_return": []}

    for ticker, group in raw_data.groupby("Ticker"):
        features = engineer_features(group)
        
        # calculam target-urile
        features["90d_return"] = (features["Close"].shift(-90) - features["Close"]) / features["Close"] * 100
        features["180d_return"] = (features["Close"].shift(-180) - features["Close"]) / features["Close"] * 100
        features["365d_return"] = (features["Close"].shift(-365) - features["Close"]) / features["Close"] * 100

        # Eliminam randurile care contin nan
        features.dropna(inplace=True)
        features_list.append(features)

    # combinam toate datele
    combined_features = pd.concat(features_list)

    # salvam datele prelucrate intr-un csv
    combined_features.to_csv("data/processed_training_data.csv", index=False)

    # punem coloanele care ne intereseaza in feature_columns
    feature_columns = [
        "pct_change", "volatility", "lag_1", "lag_7", "lag_14", "lag_30",
        "rolling_mean_7", "rolling_std_30"
    ]
    
    # antrenam modelele
    for target, model_path in zip(
        ["90d_return", "180d_return", "365d_return"],
        ["models/model_90d.pkl", "models/model_180d.pkl", "models/model_365d.pkl"]
    ):
        X = combined_features[feature_columns]
        y = combined_features[target]

        # impartim datele in setul de antrenare si cel de testare
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # antrenam modelul RandomForestRegressor care este bun pentru datele neliniare
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        # salvam modelul
        with open(model_path, "wb") as f:
            pickle.dump(model, f)

        print(f"Model for {target} saved to {model_path}")

if __name__ == "__main__":
    main()
