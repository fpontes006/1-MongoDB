from pymongo import MongoClient

client = MongoClient()

mydb = client.obcblog
mycol = mydb["posts"]

old_value = {"category": "Felipe"}
new_value = {"$set":{"category": "Automacao"}}

mycol.update_one(old_value,new_value)

result = mycol.find_one()

print(result)