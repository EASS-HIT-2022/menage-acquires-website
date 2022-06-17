import pymongo
from pymongo import MongoClient

myclient = MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
acquire_hist = mydb["acquire_hist"]
user_info = mydb["user_info"]

def _add_collection_aquire(data):
    result = acquire_hist.insert_one(data)
    return result

def _add_collection_user(data):
    result = user_info.insert_one(data)
    return result

def _get_user_report(username,month):
    items = acquire_hist.find({"username":username},{"month":month})
    print(items)
    return items
