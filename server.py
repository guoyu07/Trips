from flask import Flask
import IMDb
import IMDbDatabaseConnector
import json
import threading

import random


app = Flask(__name__)


def update_database():
    # update the database every 5 minutes
    t = threading.Timer(300.0, update_database)
    t.daemon = True
    t.start()

    IMDbDatabaseConnector.update()

def movieIDs_To_Json(movieIDs):
    movies = []
    for mid in movieIDs:
        movie = IMDb.get_movie_from_movieID(mid)
        movie["Price"] = random.uniform(57, 27638.6)
        movies.append(movie)

    return json.dumps(movies, indent=4)


@app.route("/search/<text>")
def search(text):
    return movieIDs_To_Json(IMDb.search_movieIDs(text))

@app.route("/popular/<int:num>")
def get_popular_movies(num):
    return movieIDs_To_Json(IMDb.get_most_popular_movieIDs(num))

@app.route("/top_rated/<int:num>")
def get_top_rated_movies(num):
    return movieIDs_To_Json(IMDb.get_top_rated_movieIDs(num))


started = False
if __name__ == "__main__" and not started:
    started = True
    update_database()
    app.run()