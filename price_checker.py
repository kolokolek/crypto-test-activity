import json

def load_portfolio():
    with open("portfolio.json") as f:
        return json.load(f)

def get_mock_prices():
    # Example static prices (normally from an API)
    return {
        "BTC": 65000,
        "ETH": 3200,
        "SOL": 150,
        "USDT": 1
    }

def calculate_value(portfolio, prices):
    total = 0
    for coin, amount in portfolio.items():
        total += amount * prices.get(coin, 0)
    return total

if __name__ == "__main__":
    portfolio = load_portfolio()
    prices = get_mock_prices()
    total_value = calculate_value(portfolio, prices)
    print(f"Your portfolio value is: ${total_value:,.2f}")
