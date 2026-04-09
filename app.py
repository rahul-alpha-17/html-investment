
from flask import Flask, render_template, request
import sys
import os

# Fix import path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from data import get_data
from portfolio import optimize_portfolio
from risk import calculate_risk

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    error = None

    if request.method == "POST":
        try:
            assets = request.form.get("assets")
            values = request.form.get("values")

            # Convert input
            assets = [a.strip() for a in assets.split(",")]
            values = list(map(float, values.split(",")))

            # Get data
            data = get_data(assets)

            # Portfolio optimization
            weights = optimize_portfolio(data)

            # Risk calculation
            risk = calculate_risk(data)

            result = {
                "risk": risk,
                "weights": weights,
            }

        except ValueError:
            error = "Enter valid numbers only"
        except Exception as e:
            error = f"Error: {e}"

    return render_template("index.html", result=result, error=error)


if __name__ == "__main__":
    app.run(debug=True)