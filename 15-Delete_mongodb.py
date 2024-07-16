from pymongo import MongoClient

client = MongoClient()

mydb = client.obcblog
mycol = mydb["posts"]

