import requests
import config

url = "https://api.yelp.com/v3/businesses/search"
header = {
    "Authorization": "Bearer " + config.api_key
}

param = {
    "term" : "Barber",
    "location" : "NYC"
}

response = requests.get(url, headers = header, params = param)

businesses = response.json()["businesses"]

names = [business["name"] for business in businesses if business["rating"] > 4]

print(names)