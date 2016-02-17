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
        print 'Crawling from cymon.io...'
        url = 'https://cymon.io/api/nexus/v1/blacklist/'
        url += adrtype + '/' + tag
        url += '/?days=' + day
        url += '&limit=' + limit
        url += '&offset=' + offset
        
        print url
        r = requests.get(url)
        raw = json.loads(r.text)
        result = raw['results']        
        print 'Count : ', len(result)
        for item in result:
            ShowProgress.show(result.index(item) + 1, len(result))
            DBHelper.updateAddress({'address': item['addr'], 
                                    'address_type': adrtype})
            
        
        
        
crawl(range(1,3), 
      ['malware'], 
      ['ip'])