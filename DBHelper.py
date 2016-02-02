from pymongo import MongoClient

client = MongoClient()

db = client['cymon']
ips = db['ips']


def insertIP(addr, date, tag):
    
    
    if (ips.count({'addr' : addr}) == 0):
        ips.insert_one({'addr' : addr})
        for t in ['malware', 'botnet', 'spam', 
                        'malicious%20activity', 'blacklist', 'dnsbl']:
            ips.update({'addr' : addr}, {'$set' : {t : []}})
    
    cursor = ips.find_one({'addr' : addr})
    ips.update( {'addr' : addr}, 
                { "$set" : 
                 { tag : cursor[tag] + [date.strftime('%m/%d/%Y')]}
                }
               )

    
def check():
    db = client['cymon']
    ips = db['ips']
    for item in ips.find():
        print item    

def getIPs():
    return ips
    

def insertResult(result):
    