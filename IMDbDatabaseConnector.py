#!/usr/bin/python3
import IMDb
import database

# a list of movie ids.
movieIDs = IMDb.get_most_popular_movieIDs(1)


# call this function to update the database
def update():
	update_database(get_movies())


def update_database(movies):
# implement updating of database here
	database.before_request_handler()
	for m in movies:
		movie = movies[m]
		database.add_trip(m, movie['Locations'], movie['Title'], 'Berlin', '2017-02-02')
	database.after_request_hander()	




def get_movies():
	movies = {}
	for i in movieIDs:
		movies[i] = IMDb.get_movie_from_movieID(i)
	return movies

if __name__ == '__main__':
	update()