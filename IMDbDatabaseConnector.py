#!/usr/bin/python3
import IMDb
import database
import subprocess

def init():
    movieIDs = IMDb.get_most_popular_movieIDs(30)
    movieIDs += IMDb.get_top_rated_movieIDs(30)

    subprocess.call(['bash', 'clean.sh'])

    update_database(get_movies(movieIDs))



def update_database(movies):
# implement updating of database here
    print("Started filling database")
    database.before_request_handler()
    database.create_tables()
    for m in movies:
        movie = movies[m]
        database.add_trip(m, movie['Locations'], movie['Title'], movie['Poster'], movie['Summary'], 'Berlin', '2017-02-02')
    database.after_request_hander()	
    print("Finished filling database")

def get_movies(movieIDs):

    movies = {}
    for i in movieIDs:
        movies[i] = IMDb.get_movie_from_movieID(i)
    return movies

def get_data():
    return database.get_data()

if __name__ == '__main__':
	update()