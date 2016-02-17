import requests
import json
import DBHelper

def crawl(date):
    url = 'https://otx.alienvault.com/otxapi/search/?q=&sort=null&limit=100&page=1'
    while True:
        r = requests.get(url)
        for pulse in r.json()["results"]:
            checkday = pulse["created"].split('T')[0]
            if checkday != date: return
            pulse_url = 'https://otx.alienvault.com/otxapi/pulses/' + pulse["id"] + '/indicators/?limit=9000&page=1'
            p_response = requests.get(pulse_url)
            data = p_response.json()["results"]
            for indicator in data:
                if indicator["type"] in ["IPv4", "IPv6", "domain"]:
                    item = {"address": indicator["indicator"],
                            "address_type": indicator["type"]}
                    DBHelper.updateAddress(item);

        url = r.json()["next"]

today = datetime.datetime.today().strftime("%Y-%m-%d")
crawl(today)
