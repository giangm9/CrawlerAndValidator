import requests
import json

def getCymonPage(tag, day, limit, offset, filename):
    print 'day   : ' + day + '   offset    : ' + offset
    print 'limit : ' + limit + ' file name : ' + filename
    url = 'https://cymon.io/api/nexus/v1/blacklist/ip/'+ tag + '/?days=3&limit=100000'
    url += '/?days=' + day
    url += '&limit=' + limit
    url += '&offset=' + offset
    
    
    r = requests.get(url)
    raw = json.loads(r.text)
    result = raw['results']
    
    fo = open('cymon/' + filename + '.txt', 'w')
        
    
    for item in result: 
        print '.',
        fo.write(item['url'] + '\n' + item['addr'] + '\n\n')
    
    fo.close()    
    print '\ndone, total : ' + str(len(result))
    
getCymonPage('malware', '3', '10000', '0', 'malware')
getCymonPage('botnet', '3', '10000', '0', 'botnet')    