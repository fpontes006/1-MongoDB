from pymongo import MongoClient

client = MongoClient()
db = client['nobel']

prizes = db["prizes"]
laureates = db["laureates"]

docs = db.laureates.find(
    filter = {},
    projection={"prizes.affiliations": 1, "_id": 0}
)
print(docs)

print(list(docs[:3]))

