#!/usr/bin/python3
import IMBb.py

# a list of hardcoded movie ids.
movieIDs = [
'tt0944947',        # Game of Thrones
]


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