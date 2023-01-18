import requests


url = "https://api.dev.me/v1-list-countries"

headers = {
    "Accept": "application/json",
    "x-api-key": "63c0098dc8bcac302e1a9eb7-faf677495919"
}

response = requests.request("GET", url, headers=headers)

data = response.json()

country_name = [item["code"] + " - " + item['name']['common'] for item in data["list"]]

# new_data = {
#     "name": data["name"]["common"],
#     "borders": data["borders"],
#     "capital": data["capital"],
#     "continents": data["continents"],
#     "currencies": data["currencies"],
#     "flags": data["flags"]["png"],
#     "languages": data["languages"],
#     "population": data["population"],
# }
#
#
# data_to_print = f"{data['name']['common']}\nBorders: {' '.join(data['borders'])} \nCapital: {''.join(data['capital'])}" \
#                 f"\nContinents: {' '.join(data['continents'])} \n" \
#                 f"Currencies: {list(list(data['currencies'].values())[0].values())[0]}\n" \
#                 f"Flags: {data['flags']['png']}" \
#                 f"\nLanguages: {' '.join(list(data['languages'].values()))} \nPopulation: {data['population']} "
#
# print(data_to_print)
