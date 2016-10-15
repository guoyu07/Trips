#!/usr/bin/env python3

import requests
import json

API_KEY = 'ja134927235879517824145636024746'

#http://partners.api.skyscanner.net/apiservices/browseroutes/v1.0/{market}/{currency}/{locale}/{originPlace}/{destinationPlace}/{outboundPartialDate}/{inboundPartialDate}?apiKey={apiKey}
autosuggest = "http://partners.api.skyscanner.net/apiservices/autosuggest/v1.0/GB/USD/EN/?query={}&apiKey={}"
browse_quotes = "http://partners.api.skyscanner.net/apiservices/browsequotes/v1.0/GB/USD/en-GB/{}/{}/{}/2017-02-15?apiKey={}"
pricing = "http://partners.api.skyscanner.net/apiservices/pricing/v1.0"
header = {"accept" : "application/json", "content-type" : "application/x-www-form-urlencoded"}


# Formats the date to yyyy-mm-dd
def dateFormat(day, month, year):
	newstring = year + "-" + month + "-" + day
	return newstring
	
def get_price(origin_query, destination_query, date_query):
	# get origin and destination airport in dict
	origin = json.loads(requests.get(autosuggest.format(origin_query, API_KEY)).text)
	destination = json.loads(requests.get(autosuggest.format(destination_query, API_KEY)).text)

	# get ids
	origin_id = origin["Places"][0]['CityId']
	destination_id = destination["Places"][0]['CityId']

	payload = {'apiKey' : API_KEY, 'country' : 'GB', 'currency': 'USD', 'locale' : 'EN', 'originplace' : origin_id, 'destinationplace' : destination_id, 'outbounddate' : date_query}
	# get result
	result = requests.post(pricing, json = payload, headers = header)
	return result.json

	#result["Quotes"][0]["MinPrice"]


print(get_price("Toronto","Berlin", "2017-02-15"))

# location_query = "Barcelona"
# locations = json.loads(requests.get(autosuggest.format(location_query, API_KEY)).text)
# print("LOCATIONS")
# print(json.dumps(locations, indent=4))

# location_id = locations["Places"][0]['CityId']
# result = json.loads(requests.get(browse_quotes.format(location_id, API_KEY)).text)

# print("QUOTES")
# print(json.dumps(result, indent=4))