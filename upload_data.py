from pymongo.mongo_client import MongoClient
import pandas as pd
import json

#url
#url
uri = "mongodb+srv://ayush:<12345>@cluster0.9visg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

#create a new client and connect to the server
client = MongoClient(uri)

#create a database and collection name 
DATABASE_NAME = "project_data"
COLLECTION_NAME = "waterfault"

df=pd.read_csv("D:\ml\SENSORPROJECT\notebooks\wafer_23012020_041211.csv")

df = df.drop("Unnamed: 0",axis=1)
json_str = df.T.to_json()

json_record=list(json.loads(json_str).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)