from flask import Flask
from flask_pymongo import PyMongo
import json
from bson.json_util import dumps
app = Flask(__name__)

user = 'admin'
password = 'bryanta1'
app.config["MONGO_URI"] = f'mongodb://{user}:{password}@ds137267.mlab.com:37267/win_codenames'
mongo = PyMongo(app)

def get_games(game_id):
    if game_id:
        game = mongo.db.games.find({"id": game_id})
        return game
    random_game = mongo.db.games.aggregate([{ "$sample": { "size": 1 } }])
    return random_game

def get_clues(clue_id):
    if clue_id:
        clue = mongo.db.games.find({"id": clue_id})
        return clue
    random_clue = mongo.db.games.aggregate([{ "$sample": { "size": 1 } }])
    return random_clue

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/games/', defaults={'game_id': None})
@app.route('/games/<game_id>/')
def games(game_id):
    game = get_games(game_id)
    return dumps(game)

@app.route('/clues/', defaults={'clue_id': None})
@app.route('/clues/<clue_id>/')
def games(clue_id):
    clue = get_clues(clue_id)
    return dumps(clue)

@app.route('/reviews/')
def reviews():
    return 'reviews'

@app.route('/create-review/', methods=['POST'])
def create_review():
    print(request)
    return 'nice'