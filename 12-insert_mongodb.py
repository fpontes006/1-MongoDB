from pymongo import MongoClient

client = MongoClient()

mydb = client.obcblog
mycol = mydb["posts"]

post1 = {
    "title": "web scraping",
    "category": "Automacao",
    "autor": {
        "name": "Rafael",
        "email": "rafael@obcblog.com"
    }
}

result = mycol.insert_one(post1)

print("Documento incluido com sucesso!")