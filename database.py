from pymongo import MongoClient


class MongoInstance:
    def __init__( self, host: str, port: int):
        self.client = MongoClient(host, port)
    
    def get_db_instance( self, db_name: str):
        return self.client[db_name]