
import yfinance as yf
import pandas as pd
import numpy as np

# ---------- GET DATA ----------
def get_data(stocks):
    data = yf.download(stocks, start="2020-01-01")['Adj Close']
    data = data.dropna()
    return data

# ---------- RISK PROFILE ----------
def get_risk(age, income, experience):
    score = 0

    if age < 30:
        score += 2
    elif age < 50:
        score += 1

    if income > 50000:
        score += 2
    else:
        score += 1

    if experience == "high":
        score += 2
    elif experience == "medium":
        score += 1

    if score >= 5:
        return "High Risk"
    elif score >= 3:
        return "Medium Risk"
    else:
        return "Low Risk"

# ---------- ANALYSIS ----------
def calculate_volatility(data):
    returns = data.pct_change().dropna()
    return returns.std()

# ---------- PORTFOLIO ----------
def optimize_portfolio(data):
    returns = data.pct_change().dropna()
    mean_returns = returns.mean()

    # Normalize weights
    weights = mean_returns / mean_returns.sum()

    return weights.to_dict()

# ---------- MAIN ----------
def main():
    try:
        print("===== AI Investment Advisory System =====")

        age = int(input("Enter Age: "))
        income = int(input("Enter Income: "))
        experience = input("Experience (low/medium/high): ").lower()

        if experience not in ["low", "medium", "high"]:
            print("Invalid experience!")
            return

        risk = get_risk(age, income, experience)

        stocks = ["AAPL", "MSFT", "GOOGL"]
        data = get_data(stocks)

        if data.empty:
            print("Error fetching data")
            return

        vol = calculate_volatility(data)
        weights = optimize_portfolio(data)

        print("\n===== RESULT =====")
        print("Risk Level:", risk)

        print("\nPortfolio Allocation:")
        for stock, weight in weights.items():
            print(f"{stock}: {round(weight, 2)}")

        print("\nMarket Volatility:")
        print(vol)

        print("\n⚠️ Disclaimer: Not financial advice")

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()