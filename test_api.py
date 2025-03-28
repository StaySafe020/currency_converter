import requests

API_KEY = "856177bbc5b7b5f9d55af71f"
url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD"
response = requests.get(url)
data = response.json()
print(data)