import requests
import json
class LlamaModel:
    def __init__(self, API_URL, headers):
        self.api_url = API_URL
        self.headers = headers
    
    def query( self, payload ):
        resp = requests.post(self.api_url, headers=self.headers, json=payload)
        return resp.json()