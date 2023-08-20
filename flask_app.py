# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, request, render_template
from flask_cors import CORS
from database import MongoInstance
import crud
import config
import json
from utils import QueryToJson
from model import ClusteringModel

# creating a Flask app
app = Flask(__name__)
CORS(app)

db = MongoInstance(uri = config.mongo_uri, db_name=config.db_name).db
fashion_cache = {}

query_processor = QueryToJson()

clustering = ClusteringModel()

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

#endpoint to get queries
@app.route('/query', methods=['POST'])
def get_matches():
    data = request.json
    
    query_str = data['query_str']
    query_json = query_processor.get_json_by_fuzzy_wuzzy(query_str)
    print('Query JSON:', query_json)
    user_dat = crud.get_user_by_username(db, data['username'])

    id_list = None

    print('User: ', user_dat)
    if user_dat is None:
        # Create new user
        user_dat = {
            "username": data['username'],
            "preference": query_json
        }

        # add to db
        crud.add_user(db, user_dat)

        print('User Data: ', user_dat)

        #search the data for this
        id_list = clustering.predict(query_json)
    
    else:
        merged_dict = query_processor.merge_json( query_json, user_dat['preference'])
        print('Merged Data: ', merged_dict)
        #set data to user
        new_user = {
            "username": data['username'],
            "preference": merged_dict
        }

        #update user
        crud.update_user_by_username(db, data['username'], new_user)

        #search the data for this
        id_list = clustering.predict(merged_dict)

    item_list = crud.get_multiple_fashion(db, id_list)
    return item_list

    
# add hello world endpoint
@app.route('/')
def home():
    return render_template("index.html")