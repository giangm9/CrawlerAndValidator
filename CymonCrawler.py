import requests
import json

class CymonCrawler:
    data = ''
    def __init__(self):
        url = 'https://cymon.io/api/dashboard/v1/recent-objects'
        raw = json.loads(requests.get(url).text)        
        self.data = raw['data']
        
    def get_arr(self, tab, index):
        result = []
        for item in self.data[tab]:
            result.append(item[index])
        return result
    
    def get_urls(self):
        return self.get_arr('recent_events', 'url')
    
    def get_ips(self):
        return self.get_arr('recent_ips', 'addr')
    
    def get_domains(self):
        return self.get_arr('recent_domains', 'name')
    
crawler = CymonCrawler()

print crawler.get_domains()
print crawler.get_ips()
print crawler.get_urls()    