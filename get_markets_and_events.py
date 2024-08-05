import json

import requests

# Get markets
markets = requests.get("https://gamma-api.polymarket.com/markets")
print(markets.json())

# Get events
events = requests.get("https://gamma-api.polymarket.com/events")
json_data = json.dumps(events.json(), indent=4)
with open("events.json", "w") as file:
    file.write(json_data)
print(
    "Data formatted and saved to events.json, look for clobTokenIds later in this tutorial"
)
