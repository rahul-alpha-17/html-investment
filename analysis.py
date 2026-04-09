def calculate_returns(data):
    return data.pct_change()

def calculate_volatility(data):
    return data.pct_change().std()