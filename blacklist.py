import requests
import json


def getPage(offset):    
    print offset
    url = 'https://cymon.io/api/nexus/v1/blacklist/ip/blacklist/?days=3&limit=10000&offset=' + offset
    r = requests.get(url)
    raw = json.loads(r.text)
    result = raw['results']
    
    fo = open('cymon/blacklist'+offset +'.txt', 'w')
    
    for item in result:
        print item
        fo.write(item['url'] + '\n' + item['addr'] + '\n\n')
    
    fo.close()
    print 'finish' + offset

for i in range(9):
    getPage(str(i*10000))