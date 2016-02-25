import requests
import json
import ShowProgress
import DBHelper



def crawl(days, tags, adrtypes):
    print 'Crawling from cymon.io...'
    print 'j'
    for day in days:
        for tag in tags:
            for adrtype in adrtypes:
                getCymonPage(str(day), tag, adrtype, '100000', '0')

        
def getCymonPage( day, tag, adrtype, limit, offset):                
        url = 'https://cymon.io/api/nexus/v1/blacklist/'
        url += adrtype + '/' + tag
        url += '/?days=' + day
        url += '&limit=' + limit
        url += '&offset=' + offset
        print 'URL: ', url
        r = requests.get(url)
        raw = json.loads(r.text)
        result = raw['results']                
        for item in result:
            print '.'
            
            ShowProgress.show(result.index(item) + 1, len(result))
            if not ('addr' in item.keys()):
                item['addr'] = item['name']
            DBHelper.updateAddress({'address': item['addr'], 
                                    'address_type': adrtype})
            print '\b'
        