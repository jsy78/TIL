import requests

url = "https://api.bithumb.com/public/ticker/BTC_KRW"

headers = {"Accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.json().get('data').get('prev_closing_price'))

