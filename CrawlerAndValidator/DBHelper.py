#===============================================================================
# db : cymon
# collection : addresses
# 
# address : ''
# address_type : ip/domain
# detections : []
#     {   
#         detected :
#         attempts :
#         time :
#         detect_type : 'url/hash'
#         value : 
#     }
#===============================================================================

from pymongo.mongo_client import MongoClient

client = MongoClient()
db = client['CymonAV']
collection = db['addresses']

def updateAddress(item):    
    row = collection.find_one({'address': item['address']})
    
    
    if row == None :        
        collection.insert({'address': item['address'],
                                 'address_type' : item['address_type'], 
                                 'detections' : []})
        row = collection.find_one({'address' : item['address']})
    
    if not('detections' in row.keys()):
        row['detections'] = []
    
    if not('detections' in item.keys()):
        item['detections'] = []    

    item['detections'] = row['detections'] + item['detections']    
    noDup = {v['value']:v for v in item['detections']}.values()
    collection.update({'address' : item['address']},
                      {"$set":{'detections': noDup}})

def getAddresses():
    result = []
    for row in collection.find():
        result.append(row)
    return result