from pymongo import MongoClient
from pymongo.server_api import ServerApi

class MongoInstance:
    def __init__( self, uri: str, db_name: str):
        try:
            self.client = MongoClient(uri, server_api=ServerApi('1'))
        # Send a ping to confirm a successful connection

        except:
            print( "Connection to MongoDB failed")
            raise Exception( "Connection to MongoDB failed")
        try:
            self.client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)
        
        self.db = self.get_db_instance(db_name)
    
    def get_db_instance( self, db_name: str):
        try:
            db = self.client[ db_name]
        except:
            print( "Failed to get database instance")
            raise Exception( "Failed to get database instance")
        return db