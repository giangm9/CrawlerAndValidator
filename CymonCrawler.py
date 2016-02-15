import requests
import json
import ShowProgress
import DBHelper


    
def crawl(days, tags, adrtypes):
        for day in days:
            for tag in tags:
                for adrtype in adrtypes:
                    getCymonPage(str(day), tag, adrtype, '100000', '0')
                    pass
        
def getCymonPage( day, tag, adrtype, limit, offset):
        print 'delta-day : ' + day     + '     tag   : ' + tag
        print 'adrtype   : ' + adrtype + '    limit : ' + limit
        print 'offset    : ' + offset
        
        url = 'https://cymon.io/api/nexus/v1/blacklist/'
        url += adrtype + '/' + tag
        url += '/?days=' + day
        url += '&limit=' + limit
        url += '&offset=' + offset
        
        print url
        r = requests.get(url)
        raw = json.loads(r.text)
        result = raw['results']        
                
        for item in result:
            ShowProgress.show(result.index(item) + 1, len(result))
            solve(item['addr'], adrtype)
        
def solve(addr, address_type):
        newItem = {'address' : addr, 'address_type': address_type}
        DBHelper.updateAddress(newItem)
        
crawl(range(1,2), ['malware'], ['ip'])