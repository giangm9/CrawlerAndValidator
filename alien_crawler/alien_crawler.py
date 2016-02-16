import requests
import json
import datetime
from django.utils.encoding import smart_str, smart_unicode

f = open('alien_crawler.txt', 'w')
url = "https://otx.alienvault.com/otxapi/search/?q=&sort=null&limit=1000&page=1"
r = requests.get(url)
raw = json.loads(r.text)
id = raw['results'][0]['id']


today = datetime.datetime.now()

for i in range(0,19):
    name = u'\u2019'
    name = raw['results'][i]['name']
    if raw['results'][i]['modified'][0:10] == str(today)[0:10]:
        f.write("name: " + smart_str(name) + "\n")
        f.write("created time: " + raw['results'][i]['created'] + "\n")
        f.write("modified time: " + raw['results'][i]['modified'] + "\n")
        f.write("Detail:" + "\n")


        inside_url = "https://otx.alienvault.com/otxapi/pulses/" + id + "/indicators/?limit=9000&page=1"
        inside_r = requests.get(inside_url)
        inside_raw = json.loads(inside_r.text)

        for i in range(0,inside_raw['count']):
            f.write("     type: " + inside_raw['results'][i]['type'] + "\n")
            f.write("     indicator: " + inside_raw['results'][i]['indicator'] + "\n")
            f.write("     time: " + inside_raw['results'][i]['created'] + "\n")
            f.write("       ............................................................................" + "\n")

        f.write("__________________________________________________________________________________________" + "\n")

f.close()