from flask import Flask
from flask_pymongo import PyMongo
import json
import os
from bson.json_util import dumps
from flask_cors import CORS, cross_origin

app = Flask(__name__)


# CORS
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# DB connection
username = os.getenv("MONGO_USERNAME")
password = os.getenv("MONGO_PASSWORD")
app.config["MONGO_URI"] = f'mongodb://{username}:{password}@ds137267.mlab.com:37267/win_codenames'
mongo = PyMongo(app)

PREFIX = "/api"

def get_games(game_id):
    if game_id:
        game = mongo.db.games.find({"id": game_id})
        return game
    random_game = mongo.db.games.aggregate([{ "$sample": { "size": 1 } }])
    return random_game

def get_clues(clue_id):
    if clue_id:
        clue = mongo.db.clues.find({"id": clue_id})
        return clue
    random_clue = mongo.db.clues.aggregate([{ "$sample": { "size": 1 } }])
    return random_clue

@app.route(PREFIX + '/games/', defaults={'game_id': None})
@app.route(PREFIX + '/games/<game_id>/')
def games(game_id):
    game = get_games(game_id)
    return dumps(game)

@app.route(PREFIX + '/clues/', defaults={'clue_id': None})
@app.route(PREFIX + '/clues/<clue_id>/')
def clues(clue_id):
    clue = get_clues(clue_id)
    return dumps(clue)

@app.route(PREFIX + '/reviews/')
def reviews():
    return 'reviews'

@app.route(PREFIX + '/create-review/', methods=['POST'])
def create_review():
    print(request)
    return 'nice'
