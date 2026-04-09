
from pypfopt import EfficientFrontier, expected_returns, risk_models

def optimize_portfolio(data):
    try:
        # Expected returns
        mu = expected_returns.mean_historical_return(data)

        # Risk (covariance)
        S = risk_models.sample_cov(data)

        # Optimization
        ef = EfficientFrontier(mu, S)
        ef.max_sharpe()

        weights = ef.clean_weights()
        return weights

    except Exception as e:
        print("Error:", e)
        return {}