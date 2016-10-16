#!/usr/bin/python3
import requests
import json
from bs4 import BeautifulSoup

BASE_URL = 'http://www.imdb.com'
SEARCH_URL = '/find?ref_=nv_sr_fn&q={}'


def get_movieIDs_from_list(url, numMovies):
    if numMovies < 1:
        return []
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')
    elements = [i for i in soup.find('tbody', 'lister-list')('td', 'titleColumn')]
    if numMovies >= len(elements):
        numMovies = len(elements)-1;

    return [i('a')[0]['href'].split('/')[2] for i in elements[0:numMovies]]


def get_top_rated_movieIDs(numMovies = 10):
    return get_movieIDs_from_list(BASE_URL + '/chart/top', numMovies)

def get_most_popular_movieIDs(numMovies = 10):
    return get_movieIDs_from_list(BASE_URL + '/chart/moviemeter', numMovies)

def get_search_url(searchAfter):
    searchAfter = searchAfter.lower()
    searchAfter.replace(' ', '+')
    return BASE_URL + SEARCH_URL.format(searchAfter)

def search_movieIDs(searchAfter):
    result = requests.get(get_search_url(searchAfter))
    soup = BeautifulSoup(result.text, 'html.parser')
    resultEntries = soup.find('table', 'findList')('tr')
    return [i('a')[0]['href'].split('/')[2] for i in resultEntries]

def get_movie_from_movieID(mid):
    url = BASE_URL + "/title/" + mid;
    movie = {}

    movie['Locations'] = get_locations_from_movieUrl(url)
    if movie['Locations'] == None: return {}

    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')

    movie['Title'] = get_title_from_soup(soup)
    movie['Summary'] = get_summary_from_soup(soup)
    movie['Poster'] = get_poster_from_soup(soup)

    print(json.dumps(movie, indent=4))

    return movie

def get_url_from_movieID(mid):
    return BASE_URL + "/title/" + mid;

def get_title_from_soup(soup):
    return soup.find('div', 'title_wrapper')('h1', itemprop='name')[0].text

def get_summary_from_soup(soup):
    return soup.select('#titleStoryLine')[0].find('div', 'inline canwrap')('p')[0].text

def get_poster_from_soup(soup):
    return soup.find('div', 'poster')('a')[0]('img')[0]['src']



def get_locations_from_movieUrl(url):
    try:
        url += '/locations'
        result = requests.get(url)
        soup = BeautifulSoup(result.text, 'html.parser')

        return [i.text[:-1] for i in soup.select('#filming_locations_content')[0]('a', itemprop='url')]
    except Exception:
        return None



if __name__ == '__main__':
    gotID = 'tt0944947'

    #for location in get_locations_from_movieID(gotID):
    #    print(location)
    print(get_movie_from_movieID(get_most_popular_movieIDs(1)[0]))