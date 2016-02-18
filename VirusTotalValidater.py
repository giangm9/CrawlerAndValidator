import DBHelper
import requests
from bs4 import BeautifulSoup

# TODO:
# complete the id lists

urlDivIDs = ['detetected-urls']
fileDivIDs = ['detected-downloaded']

def __getAddressesFromDB():
    return DBHelper.getAddresses()
    pass

def validateAll():
    print 'Valdating all of addresses..'
    for address in __getAddressesFromDB():
        validateAddress(address)

def validateAddress(address):
    print 'Current address : ', address['address'], '   Type : ', address['address_type']
    
    print 'Crawling from virustotal.com : ',
    detections = __getDetections(
                    __getDetectedSoups(
                        __getSoupFromAddresses(address)))    
    print 'OK'
    address.update({'detections' : detections})
    DBHelper.updateAddress(address);    
    

def __getSoupFromAddresses(address):
    url = 'https://www.virustotal.com/vi/'
    url += {'ip' : 'ip-address', 'domain' : 'domain'}[address['address_type']]
    url += '/' + address['address']
    url += '/information'
    print 'URL: ', url
    
    headers = {'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
           'accept-encoding':'gzip, deflate, sdch',
           'accept-language':'vi,en;q=0.8',
           'cache-control':'max-age=0',
           'cookie':'__utmt=1; VT_PREFERRED_LANGUAGE=en; __utma=194538546.508165789.1453801379.1454133997.1454134465.7; __utmb=194538546.18.10.1454134465; __utmc=194538546; __utmz=194538546.1454134465.7.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
           'upgrade-insecure-requests':'1',
           'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36}'}
    r = requests.get(url, headers=headers)
    return BeautifulSoup(r.text, 'html.parser')

def __getDetectedSoups(soup):
    detectIds = urlDivIDs + fileDivIDs    
    # find detections html    
    detetections = []
    for divId in detectIds:
        scope = soup.find('div', {'id' : divId})
        if scope == None:
            continue
        show = scope.find_all('div', {'class' : 'enum '})
        hide = scope.find_all('div', {'class' : 'enum  hide'})
        detetections += show + hide
    return detetections

def __getDetections(detectedSoups):
    detections = []    
    for item in detectedSoups:
        # detected/attempts
        countSoup = item.find('span', {'class' : 'text-red vt-width-5'})
        if countSoup == None:
            countSoup = item.find('span', {'class' : 'text-green vt-width-5'})        
        text = countSoup.text
        pos = text.find('/')
        deteted = text[:pos]
        attempts = text[pos + 1:]
        
        # time
        detectedDate = item.find('span', {'class' : None}).text
        
        # detect_type
        detectType = ''
        parentID = item.parent['id']
        if parentID in urlDivIDs:
            detectType = 'url'
        else:
            detectType = 'hash'
        
        #value
        value = item.find('a').text.strip()
        detections.append({'detected': deteted, 
                           'attempts': attempts, 
                           'time': detectedDate, 
                           'detected_type': detectType, 
                           'value' : value})
    return detections    

