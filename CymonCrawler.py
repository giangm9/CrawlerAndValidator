import requests
import json
import DBHelper
from datetime import date,timedelta


class CymonCrawler:
    
    def __init__(self):
        pass
    
    def crawl(self):
        self.iplist = []
        for i in range(1,2):
            for tag in ['malware']:#, 'botnet', 'spam', 
                        #'malicious%20activity', 'blacklist', 'dnsbl']:
                self.__getCymonPage(tag, str(i), '100000', '0')
        return
    
    def __getCymonPage(self, tag, day, limit, offset):
        print 'day   : ' + day + '   offset    : ' + offset
        print 'limit : ' + limit
        url = 'https://cymon.io/api/nexus/v1/blacklist/ip/' + tag
        url += '/?days=' + day
        url += '&limit=' + limit
        url += '&offset=' + offset
        
        r = requests.get(url)
        raw = json.loads(r.text)
        result = raw['results']
        count, linelimt = 0, 60
        for item in result: 
            print '.',
            count += 1
            if count > linelimt:
                count = 0
            DBHelper.insertIP(item['addr'], date.today() - timedelta(days=int(day)), tag)                                    
        print '\ndone, total : ' + str(len(result))

c = CymonCrawler()
c.crawl()

DBHelper.check()