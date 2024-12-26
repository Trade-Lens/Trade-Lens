import streamlit as st
from streamlit_echarts import st_echarts
from api.analyst_recommendation import get_analyst_recommendation

def display_stacked_bar(stock):
    rec = get_analyst_recommendation(stock)
    if rec is not None:
        
        periods = [item["period"] for item in rec]
        buy = [item["buy"] for item in rec]
        hold = [item["hold"] for item in rec]
        sell = [item["sell"] for item in rec]
        strong_buy = [item["strongBuy"] for item in rec]
        strong_sell = [item["strongSell"] for item in rec]

        options = {
            "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}},
            "legend": {
            "data": ["Strong Buy", "Buy", "Hold", "Strong Sell", "Sell"],
            },
            "grid": {"left": "0%", "right": "0%", "bottom": "3%", "containLabel": True},
            "yAxis": {"type": "value"},
            "xAxis": {
                "type": "category",
                "data": periods,
            },
            "series": [
            {
                "name": "Strong Buy",
                "type": "bar",
                "stack": "total",
                "label": {"show": True},
                "emphasis": {"focus": "series"},
                "data": strong_buy,
                "itemStyle": {"color": "#019104"},
            },
            {
                "name": "Buy",
                "type": "bar",
                "stack": "total",
                "label": {"show": True},
                "emphasis": {"focus": "series"},
                "data": buy,
                "itemStyle": {"color": "#00d904"},
            },
            {
                "name": "Hold",
                "type": "bar",
                "stack": "total",
                "label": {"show": True},
                "emphasis": {"focus": "series"},
                "data": hold,
                "itemStyle": {"color": "#ffc421"},
            },
            {
                "name": "Strong Sell",
                "type": "bar",
                "stack": "total",
                "label": {"show": True},
                "emphasis": {"focus": "series"},
                "data": strong_sell,
                "itemStyle": {"color": "#a8021b"},
            },
            {
                "name": "Sell",
                "type": "bar",
                "stack": "total",
                "label": {"show": True},
                "emphasis": {"focus": "series"},
                "data": sell,
                "itemStyle": {"color": "#ff2142"},
            }
            ],
        }
    
    st_echarts(options=options, height="500px")