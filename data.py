import yfinance as yf
import pandas as pd

def get_data(stocks):
    data = yf.download(stocks, start="2020-01-01")

    if data.empty:
        return pd.DataFrame()

    # FIX HERE 👇
    if "Adj Close" in data:
        data = data["Adj Close"]
    else:
        data = data["Close"]

    data = data.dropna()

    return data