import requests
import json
import DBHelper
import datetime

# Crawl all IPs and domains that modified today by Alienvault
def crawl():
    today = datetime.datetime.today().strftime("%Y-%m-%d")
    print "Start crawling: "
    pulse_num = 0
    # API request url of alienvault
    url = 'https://otx.alienvault.com/otxapi/search/?q=&sort=null&limit=100&page=1'
    while True:
        r = requests.get(url)
        
        for pulse in r.json()["results"]:
            #check if this pulse modified today
            checkday = pulse["modified"].split('T')[0]
            if checkday != today:
                print "Done"
                return
            pulse_num +=1
            print "Crawling from pulse " + str(pulse_num)

            #parse pulse's data to get all addresses, then add them to the db
            pulse_url = 'https://otx.alienvault.com/otxapi/pulses/' + pulse["id"] + '/indicators/?limit=9000&page=1'
            p_response = requests.get(pulse_url)
            data = p_response.json()["results"]
            ip_num = 0
            domain_num = 0
            for indicator in data:
                if indicator["type"] in ["IPv4", "IPv6"]:
                    ip_num +=1
                    item = {"address": indicator["indicator"],
                            "address_type": "IP"}
                    DBHelper.updateAddress(item);
                if indicator["type"] == "domain":
                    domain_num +=1
                    item = {"address": indicator["indicator"],
                            "address_type": "domain"}
                    DBHelper.updateAddress(item);
            print "Crawled " + str(ip_num) + " ip addresses and " + str(domain_num) + " domains" + "\n"

        url = r.json()["next"]
    
