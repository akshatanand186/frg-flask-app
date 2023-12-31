import unittest
from flask_app import app
from database import MongoInstance

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
    
    def test_add_convo(self):
        # send a POST request to the '/add-convo' endpoint
        response = self.app.post('/add-convo', json={'resp': 'hello'})
        self.assertEqual(response.status_code, 200)
    
    def test_get_convo(self):
        # send a GET request to the '/get-convo' endpoint
        response = self.app.get('/get-convo')
        self.assertEqual(response.status_code, 200)
    
    def test_search(self):
        # send a GET request to the '/search' endpoint with a search string
        response = self.app.get('/search?search_string=hello')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['search_string'], 'hello')

class TestMongo(unittest.TestCase):
    def setUp(self):
        self.db = MongoInstance().db
    
    def test_add_user(self):
        user = {
            "_id": "test_user",
            "name": "Test User",
            "email": "asgdqasg"
        }
        self.db.users.insert_one(user)

if __name__ == '__main__':
    unittest.main()