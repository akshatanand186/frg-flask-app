# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, request
from bson import ObjectId
import json
from database import MongoInstance
import crud
import config

# creating a Flask app
app = Flask(__name__)
db = MongoInstance(uri = config.mongo_uri, db_name=config.db_name).db
fashion_cache = {}

# create a route for '/add-convo' endpoint
@app.route('/add-convo', methods=['POST'])
def add_convo():
    #TODO: Add code to add resp to the llm conversation
    #FURTHER: use states to manage different users
    pass

# create a route for '/get-convo' endpoint
@app.route('/get-convo', methods=['GET'])
def get_convo():
    #TODO: Add code to get the llm conversation
    #FURTHER: use states to manage different users
    pass

@app.route('/search', methods=['GET'])
def search():
    search_str = request.args.get('search_str')
    # TODO: get user data
    # TODO: fetch user data and send along with the response to the correlation engine
    # TODO: get response from correlation engine
    pass

#endpoint to get fashion by id
@app.route('/fashion/<id>', methods=['GET'])
def get_fashion_by_id(id):
    if id in fashion_cache.keys():
        return fashion_cache[id]
    fashion_cache[id] = crud.get_fashion(db, id)
    return fashion_cache[id]

# add hello world endpoint
@app.route('/')
def hello_world():
    return 'Hello World!'