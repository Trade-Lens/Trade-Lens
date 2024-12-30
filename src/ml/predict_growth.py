import pickle
import pandas as pd
import streamlit as st
from ml.features import engineer_features

@st.cache_resource
def load_models():
    return {
        "90d": pickle.load(open("models/model_90d.pkl", "rb")),
        "180d": pickle.load(open("models/model_180d.pkl", "rb")),
        "365d": pickle.load(open("models/model_365d.pkl", "rb")),
    }

@st.cache_data
def predict_growth(historical_df):
    features = engineer_features(historical_df)
    feature_columns = [
        "pct_change", "volatility", "lag_1", "lag_7", "lag_14", "lag_30",
        "rolling_mean_7", "rolling_std_30"
    ]

    # selectam doar coloanele care ne intereseaza
    features = features[feature_columns]

    models = load_models()

    # facem predictiile pentru fiecare model
    predictions = {}
    for key, model in models.items():
        predictions[key] = model.predict(features.tail(1))[0]
    
    return predictions
