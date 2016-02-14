#===============================================================================
# db : Cymon
# collection : addresses
# 
# address : ''
# address_type : ip/domain
# VT_detections : []
#     {   count 
#         time 
#         detected_type : 'url/hash'
#         value : 
#     }
#===============================================================================

from pymongo.mongo_client import MongoClient

client = MongoClient()
db = client['cymon']
collection = db['addresses']

def updateAddress(item):
    row = collection.find_one({'address': item['address']})
        
    if row == None :
        row = collection.insert({'address':item['address']})
        
    try:
        new_VTDetections = row['VT_detections']    
        new_VTDetections = set(new_VTDetections + [item['VT_detect']])
        new_VTDetections = list(new_VTDetections)        
    except Exception:
        new_VTDetections = []
    
    
    
    collection.update({'address' : item['address']},
                      {"$set":
                       {'address_type' : item['address_type'],
                        'VT_detections': new_VTDetections
                        }
                       })

def getAddresses():
    result = []
    for row in collection.find():
        result.append(row['address'])
    