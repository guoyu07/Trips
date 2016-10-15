#!/usr/bin/python3
import IMBb.py

# a list of movie ids.
movieIDs = IMBb.get_top_rated_movieIDs(50)


# call this function to update the database
def update():
    update_database(get_movies())


def update_database(movies):
    # implement updating of database here
    pass


def get_movies():
    movies = {}
    for i in movieIDs:
        movies[i] = IMBb.get_movie_from_movieID(i)