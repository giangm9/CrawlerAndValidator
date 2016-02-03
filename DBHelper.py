from pymongo import MongoClient

client = MongoClient()

db = client['cymon']
ips = db['ips']
vtotal = db['vtotal']


def insertIP(addr, date, tag):
    
    
    if (ips.count({'addr' : addr}) == 0):
        ips.insert_one({'addr' : addr})
        for t in ['malware', 'botnet', 'spam', 
                        'malicious%20activity', 'blacklist', 'dnsbl']:
            ips.update({'addr' : addr}, {'$set' : {t : []}})
    
    cursor = ips.find_one({'addr' : addr})
    newlist = list(set(cursor[tag] + [date.strftime('%m/%d/%Y')]))
    ips.update( {'addr' : addr}, 
                { "$set" :
                 { tag : newlist}
                }
               )

    
def check():
    
    for item in vtotal.find():
        print item    
    for item in ips.find():
        print item
    
def getIPs():
    return ips
    

def insertResult(result):
    cursor = vtotal.find_one({'addr' : result['addr']})
    vtotal.update({'addr' : result['addr']},
                  {'$set':
                   {'detected' :cursor['detected'] + result['detected']}
                   })

    