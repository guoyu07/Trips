#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup

BASE_URL = 'http://www.imdb.com'
SEARCH_URL = '/find?q={}&s=tt&ttype=tv&ref_=fn_tv'

def get_search_url(searchAfter):
    searchAfter = searchAfter.lower()
    searchAfter.replace(' ', '%20')
    return BASE_URL + SEARCH_URL.format(searchAfter)

def search_movieIDs(searchAfter):
    result = requests.get(get_search_url(searchAfter))
    soup = BeautifulSoup(result.text, "lxml")
    resultEntries = soup.find('table', 'findList').find_all('tr')
    return [i.find_all('a')[0]['href'].split('/')[2] for i in resultEntries]

def get_movie_from_movieID(mid):
    url = BASE_URL + "/title/" + mid;
    movie = {}
    movie['Title'] = get_title_from_movieUrl(url)

    if movie['Title'] == "": return {}

    movie['Locations'] = get_locations_from_movieUrl(url)

    return movie

def get_url_from_movieID(mid):
    return BASE_URL + "/title/" + mid;


def get_title_from_movieUrl(url):
    try:
        result = requests.get(url)
        soup = BeautifulSoup(result.text, "lxml")
        return soup.find('div', 'title_wrapper')('h1', itemprop='name')[0].text
    except Exception:
        return ""


def get_locations_from_movieUrl(url):
    try:
        url += '/locations'
        result = requests.get(url)
        soup = BeautifulSoup(result.text, "lxml")

        return [i.text[:-1] for i in soup.select('#filming_locations_content')[0]('a', itemprop='url')]
    except Exception:
        return None



if __name__ == '__main__':
    gotID = 'tt0944947'

    #for location in get_locations_from_movieID(gotID):
    #    print(location)
    print(get_movie_from_movieID(gotID)['Title'])