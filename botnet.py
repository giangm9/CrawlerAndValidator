import requests
import json


def getPage(offset):    
    print offset
    url = 'https://cymon.io/api/nexus/v1/blacklist/ip/botnet/?days=3'
    r = requests.get(url)
    raw = json.loads(r.text)
    result = raw['results']
    
    fo = open('cymon/botnet.txt', 'w')
    
    for item in result:
        print item
        fo.write(item['url'] + '\n' + item['addr'] + '\n\n')
    
    fo.close()
    print 'finish' + offset


getPage('')
        


