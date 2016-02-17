import requests
import json
import datetime
from django.utils.encoding import smart_str, smart_unicode

f = open('alien_crawler.txt', 'w')

today = datetime.datetime.now()

#choose page from 1 to 5
for i in range (1,5):
    url = "https://otx.alienvault.com/otxapi/search/?q=&sort=null&limit=20&page=" + str(i)
    r = requests.get(url)
    raw = json.loads(r.text)

    #crawl all threads in day
    for i in range(0,19):
        name = u'\u2019'
        name = raw['results'][i]['name']
        id = raw['results'][i]['id']

        if raw['results'][i]['modified'][0:10] == str(today)[0:10]:
            f.write("name: " + smart_str(name) + "(id: " + str(id) + ")" + "\n")
            f.write("created time: " + raw['results'][i]['created'] + "\n")
            f.write("modified time: " + raw['results'][i]['modified'] + "\n")
            f.write("Detail:" + "\n")


            inside_url = "https://otx.alienvault.com/otxapi/pulses/" + id + "/indicators/?limit=9000&page=1"
            inside_r = requests.get(inside_url)
            inside_raw = json.loads(inside_r.text)

            #crawk info from each thread
            for i in range(0, inside_raw['count']):
                f.write("     type: " + inside_raw['results'][i]['type'] + "\n")
                f.write("     indicator: " + inside_raw['results'][i]['indicator'] + "\n")
                f.write("     time: " + inside_raw['results'][i]['created'] + "\n")
                f.write("       ............................................................................" + "\n")

            f.write("__________________________________________________________________________________________" + "\n")

f.close()