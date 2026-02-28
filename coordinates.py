import json
from geopy.geocoders import Nominatim
import time

with open("statecapitals.json", "r") as file:
    data = json.load(file)

geolocator = Nominatim(user_agent="state_capitals_project", timeout=10)

for item in data:
    address = item["address"]
    location = geolocator.geocode(address)

    if location:
        item["latitude"] = location.latitude
        item["longitude"] = location.longitude
        print("Done:", item["state"])
    else:
        item["latitude"] = None
        item["longitude"] = None
        print("Not found:", item["state"])

    time.sleep(1)   

with open("state_capitals_with_coords.json", "w") as file:
    json.dump(data, file, indent=4)

print("New file created: us_state_capitals_with_coords.json")