import requests
import json
import ShowProgress
from datetime import date,timedelta
import DBHelper

class nCymonCrawler:
    def __init__(self):
        pass
    
    def crawl(self, days, tags, adrtypes):
        for day in days:
            for tag in tags:
                for adrtype in adrtypes:
                    self.__getCymonPage(str(day), tag, adrtype, '100000', '0')
                    pass
        
    def __getCymonPage(self, day, tag, adrtype, limit, offset):
        print 'delta-day : ' + day     + '|    tag   : ' + tag
        print 'adrtype   : ' + adrtype + '|    limit : ' + limit
        print 'offset    : ' + offset
        
        url = 'https://cymon.io/api/nexus/v1/blacklist'
        url += adrtype + '/' + tag
        url += '/?days=' + day
        url += '/&limit' + limit
        url += '&offset' + offset
        
        r = requests.get(url)
        raw = json.loads(r.text)
        result = raw['result']        
                
        for item in result:
            ShowProgress.show(result.index(item), len(result))
            self.__solve(item, day, tag, adrtype)
                
        
    def __solve(self, item, day, tag, adrtype):
        ipResult = {'adrtype' : adrtype,
                    'tag' : tag,
                    'adr' : item['addr'],
                    'date' : date.today() - timedelta(days=-int(day))}
        DBHelper.insertIP(ipResult)