from flask import Flask
import IMDb
import json

app = Flask(__name__)

def movieIDs_To_Json(movieIDs):
    movies = {}
    for mid in movieIDs:
        movies[mid] = IMDb.get_movie_from_movieID(mid)

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



if __name__ == "__main__":
    app.run()