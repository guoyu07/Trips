#!/usr/bin/env python3

import requests
import json

API_KEY = "ja134927235879517824145636024746"
autosuggest = "http://partners.api.skyscanner.net/apiservices/autosuggest/v1.0/ES/USD/EN/?query={}&apiKey={}"

location_query = "Barcelona"
locations = json.loads(requests.get(autosuggest.format(location_query, API_KEY)).text)
print("LOCATIONS")
print(json.dumps(locations, indent=4))

location_id = locations["Places"][0]['CityId']
browse_quotes = "http://partners.api.skyscanner.net/apiservices/browsequotes/v1.0/ES/USD/en-GB/{}/CDG/2017-02-11/2017-02-15?apiKey={}"
result = json.loads(requests.get(browse_quotes.format(location_id, API_KEY)).text)

print("QUOTES")
print(json.dumps(result, indent=4))