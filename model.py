from sklearn.cluster import KMeans
from joblib import dump, load
import numpy as np
from sklearn.preprocessing import LabelEncoder
import pandas as pd

class ClusteringModel:
    def __init__(self):
        self.model = load('kmeans.joblib')
        self.cluster_map = load('cluster_map.joblib')
        self.label_encoders = load('label_encoders.joblib')
        self.col_list = [
            'gender', 'subCategory', 'articleType', 'baseColour', 'usage'
        ]
    def predict(self, data):
        x = []
        for col in self.label_encoders.keys():
            x.append(  self.label_encoders[col].transform([data[col]])[0]  )
        
        cluster = self.model.predict([x])[0]

        # get all ids corresponding to cluster in pandas cluster_map
        ids = self.cluster_map[self.cluster_map['cluster'] == cluster]['id'].tolist()

        return ids
