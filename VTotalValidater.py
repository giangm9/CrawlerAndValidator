
        
def getData(soup, divID):
    dataScope = soup.find('div', {'id' : divID})    
    return dataScope.find_all('div', {'class': 'enum '})        
    
def addSimple(newElement, item):
    count = item.find('span', {'class':'text-red vt-width-5' })
    date = item.find('span', {'class': None})    
    newElement['count'] = count.getText().strip()
    newElement['date'] = date.getText().strip()
                           
def getDetectedUrls(soup):
    result = []
    for item in getData(soup, 'detected-urls'):
        newElement = {}
        addSimple(newElement, item)
        url = item.find('a')
        newElement['hosted-url'] = url.getText().strip()
        result.append(newElement)

    return result

def getDetectedDownload(soup):
    result = []
    for item in getData(soup, 'detected-downloaded'):
        newElement = {}
        addSimple(newElement, item)
        url = item.find('a')
        newElement['hashKey'] = url.getText().strip()
        result.append(newElement)

    return result

def getUnDetectedDownload(soup):
    result = []
    for item in getData(soup, 'undetected-downloaded'):
        newElement = {}
        addSimple(newElement, item)
        url = item.find('a')
        newElement['hashKey'] = url.getText().strip()
        result.append(newElement)

    return result

def getDetectedCommunicating(soup):
    result = []
    for item in getData(soup, 'detected-communicating'):
        newElement = {}
        addSimple(newElement, item)
        url = item.find('a')
        newElement['hashKey'] = url.getText().strip()
        result.append(newElement)

    return result


def getUnDetectedCommunicating(soup):
    result = []
    for item in getData(soup, 'undetected-communicating'):
        newElement = {}
        addSimple(newElement, item)
        url = item.find('a')
        newElement['hashKey'] = url.getText().strip()
        result.append(newElement)

    return result
