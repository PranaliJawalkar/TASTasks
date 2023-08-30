import requests
from forex_python.converter import CurrencyRates

def get_exchange_rate(api_key, from_currency, to_currency):
    url = f"https://v6.exchangeratesapi.io/latest?base={from_currency}&symbols={to_currency}&apiKey={api_key}"
    response = requests.get(url)
    data = response.json()
    return data['rates'][to_currency]

def main():
    api_key = "YOUR_EXCHANGE_RATES_API_KEY"  # Replace with your actual API key
    c = CurrencyRates()

    amount = float(input("Enter the amount: "))
    from_currency = input("Enter the source currency (e.g., USD): ").upper()
    to_currency = input("Enter the target currency (e.g., EUR): ").upper()

    try:
        exchange_rate = get_exchange_rate(api_key, from_currency, to_currency)
        converted_amount = c.convert(from_currency, to_currency, amount)
        
        print(f"{amount:.2f} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
    except KeyError:
        print("Error: Currency conversion not available for the specified pair.")

if __name__ == "__main__":
    main()
