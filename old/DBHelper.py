from pymongo import MongoClient

client = MongoClient()

db = client['cymon']
vtotal = db['vtotal']


def insertIP(adr):
    col = db[adr['adrtype']]
    address = adr['adr']
    if (col.count({'addr' : address}) == 0):
        col.insert_one({'addr' : address})
        for t in ['malware', 'botnet', 'spam', 
                        'malicious%20activity', 'blacklist', 'dnsbl']:
            col.update({'addr' : adr['adr']}, {'$set' : {t : []}})
    
    cursor = col.find_one({'addr' : address})
    newlist = list(set(cursor[adr['tag']] + [adr['date'].strftime('%m/%d/%Y')]))
    col.update( {'addr' : address}, 
                { "$set" :
                 { adr['tag'] : newlist}
                }
               )
    
def check():
    
    for item in vtotal.find():
        print item    
    
    
def getIPs():
    db.ips.find()
    

def insertResult(result):
    print result
#     cursor = vtotal.find_one({'addr' : result['addr']})
#     vtotal.update({'addr' : result['addr']},
#                   {'$set':
#                    {'detected' : cursor['detected'] + result['detected']}
#                    })

    