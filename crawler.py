import requests
import json

def getCymonPage(tag, day, limit, offset, filename):
    print 'day   : ' + day + '   offset    : ' + offset
    print 'limit : ' + limit + ' file name : ' + filename
    url = 'https://cymon.io/api/nexus/v1/blacklist/ip/'+ tag
    url += '/?days=' + day
    url += '&limit=' + limit
    url += '&offset=' + offset
    
    
    r = requests.get(url)
    raw = json.loads(r.text)
    result = raw['results']
    
    fo = open('cymon/' + filename + '.txt', 'w')
        
    
    for item in result: 
        print '.',
        fo.write(item['addr'] + '\n')
    
    fo.close()    
    print '\ndone, total : ' + str(len(result))
    
getCymonPage('malware', '1', '100000', '0', 'malware1')
getCymonPage('malware', '2', '100000', '0', 'malware2')
getCymonPage('malware', '3', '100000', '0', 'malware3')

getCymonPage('botnet', '1', '100000', '0', 'botnet1')
getCymonPage('botnet', '2', '100000', '0', 'botnet2')
getCymonPage('botnet', '3', '100000', '0', 'botnet3')

getCymonPage('spam', '1', '100000', '0', 'spam1')
getCymonPage('spam', '2', '100000', '0', 'spam2')
getCymonPage('spam', '3', '100000', '0', 'spam3')

getCymonPage('phishing', '1', '100000', '0', 'phishing1')
getCymonPage('phishing', '2', '100000', '0', 'phishing2')
getCymonPage('phishing', '3', '100000', '0', 'phishing3')

getCymonPage('malicious%20activity', '1', '100000', '0', 'malicious%20activity1')
getCymonPage('malicious%20activity', '2', '100000', '0', 'malicious%20activity2')
getCymonPage('malicious%20activity', '3', '100000', '0', 'malicious%20activity3')

getCymonPage('blacklist', '1', '100000', '0', 'blacklist1')
getCymonPage('blacklist', '2', '100000', '0', 'blacklist2')
getCymonPage('blacklist', '3', '100000', '0', 'blacklist3')

getCymonPage('dnsbl', '1', '100000', '0', 'dnsbl1')
getCymonPage('dnsbl', '2', '100000', '0', 'dnsbl2')
getCymonPage('dnsbl', '3', '100000', '0', 'dnsbl3')