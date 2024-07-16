from pymongo import MongoClient

client = MongoClient()
db = client['nobel']

prizes = db["prizes"]
laureates = db["laureates"]

walter = db.laureates.find_one({
    'firstname': 'Walter',
    'surname': 'Kohn',
    
})
print(walter)

san_francisco = db.laureates.count_documents({
    'prizes.affiliations.city': 'San Francisco, CA'
})
print(san_francisco)

no_country = db.laureates.count_documents({
    'bornCountry':{
        '$exists': False
    }
})
print(no_country)

