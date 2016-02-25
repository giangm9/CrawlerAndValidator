import requests
import json
import ShowProgress
import DBHelper



def crawl(days, tags, adrtypes):
    print 'Crawling from cymon.io...'    
    for day in days:
        for tag in tags:
            for adrtype in adrtypes:
                for i in range(10):                    
                    limit = 10000
                    count = getCymonPage(str(day), tag, adrtype, str(limit), str(i*1000))
                    if (limit * i) > count :
                        break;

        
def getCymonPage( day, tag, adrtype, limit, offset):                
        url = 'https://cymon.io/api/nexus/v1/blacklist/'
        url += adrtype + '/' + tag
        url += '/?days=' + day
        url += '&limit=' + limit
        url += '&offset=' + offset
        print 'URL: ', url
        
        headers = {'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
           'accept-encoding':'gzip, deflate, sdch',
           'accept-language':'vi,en;q=0.8',
           'cache-control':'max-age=0',
           'cookie':'__utmt=1; VT_PREFERRED_LANGUAGE=en; __utma=194538546.508165789.1453801379.1454133997.1454134465.7; __utmb=194538546.18.10.1454134465; __utmc=194538546; __utmz=194538546.1454134465.7.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
           'upgrade-insecure-requests':'1',
           'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36}'}
        r = requests.get(url, headers)
        raw = json.loads(r.text)
        result = raw['results']
        if len(result) == 0:
            print '\t\b'
        for item in result:                        
            ShowProgress.show(result.index(item) + 1, len(result))
            if not ('addr' in item.keys()):
                item['addr'] = item['name']
            DBHelper.updateAddress({'address': item['addr'], 
                                    'address_type': adrtype})
        
        return raw['count']    