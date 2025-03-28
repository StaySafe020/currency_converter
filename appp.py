import streamlit as st
import requests
from dotenv import load_dotenv
import os

load_dotenv()

# Get API key from environment
API_KEY = os.getenv("API_KEY")
def get_exchange_rate(base_currency, target_currency, api_key):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200 and data["result"] == "success":
        return data["conversion_rates"][target_currency]
    else:
        raise Exception("Error fetching exchange rates")

# Function to convert currency
def convert_currency(amount, base_currency, target_currency, api_key):
    rate = get_exchange_rate(base_currency, target_currency, api_key)
    return amount * rate

# Function to get all available currencies
def get_all_currencies(api_key):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200 and data["result"] == "success":
        return list(data["conversion_rates"].keys())
    else:
        raise Exception("Error fetching currency list")

def main():
    st.title("Currency Converter")

    # Fetch available currencies
    try:
        currencies = get_all_currencies(API_KEY)
    except Exception as e:
        st.error(f"Could not load currencies: {str(e)}")
        return

    # Input fields
    amount = st.number_input("Enter amount", min_value=0.01, value=1.0)
    base_currency = st.selectbox("From currency", currencies)
    target_currency = st.selectbox("To currency", currencies)

    # Conversion button
    if st.button("Convert"):
        try:
            result = convert_currency(amount, base_currency, target_currency, API_KEY)
            st.success(f"{amount} {base_currency} = {result:.2f} {target_currency}")
        except Exception as e:
            st.error(f"Error: {str(e)}")

if __name__ == "__main__":
    main()