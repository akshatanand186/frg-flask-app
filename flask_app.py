# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, jsonify, request
from database import MongoInstance

# creating a Flask app
app = Flask(__name__)

# connect to database (make sure the database is created)
test_db = MongoInstance('localhost', 27017).get_db_instance('test_db')

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

# add hello world endpoint
@app.route('/')
def hello_world():
    return 'Hello World!'