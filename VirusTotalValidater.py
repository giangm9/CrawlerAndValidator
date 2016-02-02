from bs4 import BeautifulSoup
import requests
import DBHelper
class VTValidater:
    def __init__(self):
        pass
    
    def importData(self):
        self.ips = DBHelper.getIPs()

    def exportData(self):
        for ipaddr in self.ips:
            DBHelper.insertResult({'ipaddr' : ipaddr, 
                                   'detected' : self.__getDetected()})
    
    def __getHtml(self, ipaddr):
        url = 'https://www.virustotal.com/vi/ip-address/'
        url += ipaddr
        url += '/information'
        headers = {'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
               'accept-encoding':'gzip, deflate, sdch',
               'accept-language':'vi,en;q=0.8',
               'cache-control':'max-age=0',
               'cookie':'__utmt=1; VT_PREFERRED_LANGUAGE=en; __utma=194538546.508165789.1453801379.1454133997.1454134465.7; __utmb=194538546.18.10.1454134465; __utmc=194538546; __utmz=194538546.1454134465.7.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
               'upgrade-insecure-requests':'1',
               'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36}'}
        r = requests.get(url, headers = headers)
        self.soup = BeautifulSoup(r.text, 'html.parser')
    
    def __getData(self, divID):
        dataScope = self.soup.find('div', {'id' : divID})
        
        show = dataScope.find_all('div', {'class': 'enum '})
        hide = dataScope.find_all('div', {'class': 'enum  hide'})
        return show + hide
    
    def __addBase(self, newE, item):
        count = item.find('span', {'class':'text-red vt-width-5' })
        date = item.find('span', {'class': None})    
        newE['count'] = count.getText().strip()
        newE['date'] = date.getText().strip()        
        
    def __getBaseInfo(self, ids):
        result = []
        for divID in ids:
            for item in self.__getData(divID):
                newE = {}
                self.__addBase(newE, item)
                result.append(newE)
        return result
        
    def __getDetected(self):
        return self.__getBaseInfo(['detected-urls'])