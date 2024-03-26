import requests


class PriceRateController:

    def fetch_price_rate(self, from_currency: str, to_currency: str):
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={from_currency}&vs_currencies={to_currency}"
        response = requests.get(url)
        data = response.json()
        if "solana" in data:
            return data[from_currency][to_currency]
        return None
