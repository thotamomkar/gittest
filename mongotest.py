import pymongo
client = pymongo.MongoClient("mongodb+srv://logan:logan786@cluster0.d07rw.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"Omkar",
    "email" : "omkar@ineuron.ai",
    "surname" : "Thotam"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)