import requests
import json

def validate(indicator):
    payload = { 'url': indicator }
    headers = { 'accept': 'application/json, text/javascript, */*; q=0.01',
                'accept-encoding': 'gzip, deflate',
                'accept-language': 'vi-VN,vi;q=0.8,fr-FR;q=0.6,fr;q=0.4,en-US;q=0.2,en;q=0.2',
                'content-length': str(len(indicator)+4),
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': 'VT_PREFERRED_LANGUAGE=vi; __utmt=1; __utma=194538546.1212458640.1454253902.1455476628.1455478979.14; __utmb=194538546.1.10.1455478979; __utmc=194538546; __utmz=194538546.1454313489.2.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
                'origin': 'https://www.virustotal.com',
                'referer': 'https://www.virustotal.com/vi/',
                'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36',
                'x-csrftoken': 'null',
                'x-requested-with': 'XMLHttpRequest' }

    r = requests.post('https://www.virustotal.com/vi/url/submission/', headers=headers, data=payload)
    sumup_data = r.json()
    out_stream.write("indicator: " + indicator)
    out_stream.write("positives: " + str(sumup_data["positives"]) + "\n")
    out_stream.write("total: " + str(sumup_data["total"]) + "\n")
    out_stream.write("first analysis: " + sumup_data["first_analysis_date"] + "\n")
    out_stream.write("last analysis: " + sumup_data["last_analysis_date"] + "\n")
    out_stream.write("url: " + sumup_data["last_analysis_url"] + "\n")
    out_stream.write("\n")

in_ip = open("IPv4.txt", "r")
in_domain = open("domain.txt", "r")
out_stream = open("result.txt", "w")
for ip in in_ip:
    validate(ip)
for domain in in_domain:
    validate(domain)
