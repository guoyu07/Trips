import requests
import json

loc = "http://dev.virtualearth.net/REST/v1/Locations?query={}&key={}"
key = 'Aoc49e5_BfxNsKh3P3EJ5VdkYHJcc0hW7wM8ldWYPXXKSymk7fCFc93_ZTsXsCZ0'

search = "http://dev.virtualearth.net/REST/v1/Locations?query={}&userLocation={},{}&includeNeighborhood=1&key={}"

query = 'White%20House'
#query = 'Magheramorne Quarry, Larne, County Antrim, Northern Ireland, UK'

#print(json.loads(requests.get(loc.format(query, key)).text))
user_l = json.loads(requests.get(loc.format(query, key)).text)['resourceSets'][0]['resources'][0]['point']['coordinates']

#print(user_l[0])

print(json.loads(requests.get(search.format('airport', user_l[0], user_l[1], key)).text))