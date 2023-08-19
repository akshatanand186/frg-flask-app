# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, jsonify, request
from database import MongoInstance

# creating a Flask app
app = Flask(__name__)

# connect to database (make sure the database is created)
test_db = MongoInstance('localhost', 27017).get_db_instance('test_db')