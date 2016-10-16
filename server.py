from flask import Flask
import IMDb
import IMDbDatabaseConnector
import json
import threading
import movieposterfind
import database

import random


app = Flask(__name__)


def update_database():
    # update the database every 5 minutes
    t = threading.Timer(30.0, update_database)
    t.daemon = True
    t.start()



@app.route("/get")
def search():
    return IMDbDatabaseConnector.get_data()

@app.route("/pic/<query>")
def get_popular_movies(query):
    return movieposterfind.bing_search(query)


started = False
if __name__ == "__main__" and not started:
    started = True
    IMDbDatabaseConnector.init()

    app.run()
