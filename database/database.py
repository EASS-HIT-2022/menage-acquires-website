import pymongo
from pymongo import MongoClient

myclient = MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
acquire_hist = mydb["acquire_hist"]
client_hist = mydb["client_hist"]

mylist = [
    {"client name": "string", "aquire": "260"},
    {"clientname": "shiran", "aquire": "1500"},
    {"clientname": "ff", "aquire": "sd"}
    ]

def _add_collection_aquire(data):
    x= acquire_hist.insert_one(data)
    print(x.inserted_ids)

