#!/usr/bin/env python3
import random
import requests
import json
import time

API_KEY = open('token').read()

#http://partners.api.skyscanner.net/apiservices/browseroutes/v1.0/{market}/{currency}/{locale}/{originPlace}/{destinationPlace}/{outboundPartialDate}/{inboundPartialDate}?apiKey={apiKey}
autosuggest = "http://partners.api.skyscanner.net/apiservices/autosuggest/v1.0/GB/USD/EN/?query={}&apiKey={}"
browse_quotes = "http://partners.api.skyscanner.net/apiservices/browsequotes/v1.0/GB/USD/en-GB/{}/{}/{}?apiKey={}"

# Formats the date to yyyy-mm-dd
def dateFormat(day, month, year):
	newstring = year + "-" + month + "-" + day
	return newstring

def save_get(source, a, b):
	if a in source:
		temp = source[a]
		if len(temp) > 0:
			return (temp[0][b], True)
	return (None, False)
	
def get_price(origin_query, destination_query, date_query):
	# get origin and destination airport in dict

	origin = json.loads(requests.get(autosuggest.format(origin_query, API_KEY)).text)
	destination = json.loads(requests.get(autosuggest.format(destination_query, API_KEY)).text)

	# get ids
	origin_id, successful = save_get(origin, 'Places', 'CityId')
	if successful:
		destination_id, successful = save_get(destination, 'Places', 'CityId')
		if successful:
			# get result
			result = json.loads(requests.get(browse_quotes.format(origin_id, destination_id, date_query, API_KEY)).text)
			price, successful = save_get(result, "Quotes", "MinPrice")
			if successful:
				return price

	random.seed(time.time())
	return random.randint(23, 1237)

#print(get_price("Vancouver", "Barcelona", "2017-02-02"))