import requests


url = "https://api.dev.me/v1-list-countries"

headers = {
    "Accept": "application/json",
    "x-api-key": "63c0098dc8bcac302e1a9eb7-faf677495919"
}

response = requests.request("GET", url, headers=headers)

my_data = response.json()["list"]

# list with all country code and full country name
country_name = [item["code"] + " - " + item['name']['common'] for item in my_data]
