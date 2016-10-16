#!/usr/bin/env python3

import requests
import json

API_KEY = open('token').read()

#http://partners.api.skyscanner.net/apiservices/browseroutes/v1.0/{market}/{currency}/{locale}/{originPlace}/{destinationPlace}/{outboundPartialDate}/{inboundPartialDate}?apiKey={apiKey}
autosuggest = "http://partners.api.skyscanner.net/apiservices/autosuggest/v1.0/GB/USD/EN/?query={}&apiKey={}"
browse_quotes = "http://partners.api.skyscanner.net/apiservices/browsequotes/v1.0/GB/USD/en-GB/{}/{}/{}?apiKey={}"

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

	# get result
	result = json.loads(requests.get(browse_quotes.format(origin_id, destination_id, date_query, API_KEY)).text)
	return result["Quotes"][0]["MinPrice"]

#print(get_price("Boston", "Barcelona", "2017-02-02"))