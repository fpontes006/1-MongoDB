from pymongo import MongoClient

client = MongoClient()
db = client['nobel']

prizes = db["prizes"]
laureates = db["laureates"]

print(db.laureates.distinct('gender'))
print(db.laureates.distinct('prizes.category'))