### As of now you just need to change the query and youll get a image-url from
### bing_search


import urllib
import urllib2
import json

print("works until here")
 
def main():
    movie = "Lord of the rings the return of the king"
    query =  movie + "Movie Poster"
    print (query)

    #print bing_search(query, 'Web')
    print bing_search(query, 'Image')
 
def bing_search(query, search_type):
    search_type = 'Image' 
    key= 'OnxQM0p1rgGWyKf5ShtHvpVuClj3eJcPVNENs1dzo8I'
    query = urllib.quote(query)
    # create credential for authentication
    credentials = (':%s' % key).encode('base64')[:-1]
    auth = 'Basic %s' % credentials
    url = 'https://api.datamarket.azure.com/Data.ashx/Bing/Search/'+search_type+'?Query=%27'+query+'%27&$top=5&$format=json'
    request = urllib2.Request(url)
    request.add_header('Authorization', auth)
    request_opener = urllib2.build_opener()
    response = request_opener.open(request) 
    response_data = response.read()
    json_result = json.loads(response_data)
    result_list = json_result['d']['results']
    return result_list[0]['MediaUrl']



 
if __name__ == "__main__":
    main()
