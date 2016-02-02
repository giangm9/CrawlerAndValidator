from pymongo import MongoClient

client = MongoClient()

print client.database_names()

db = client['virustotal']
collection = db['ipscan']

doc = {'name' : 'dan', 'age' : 16, 'language' : ['C++', 'Java', 'python'] }

db['users'].insert(doc)

print db['users'].find_one()


