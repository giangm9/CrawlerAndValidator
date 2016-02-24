PROJECT NAME
------------
Construction Crawler from the site to provide resources about the Malicious

INTRODUCTION
------------

Included:
All source files(.py):
- AVcrawler.py
- CymonCrawler.py
- DBHelper.py
- DailyCrawler.py
- ShowProgess.py
- VirusTotalValidater.py
- __init__.py
- setup.py
This project use python 2.7 and beatifulsoup to crawl information from https://otx.alienvault.com/browse, https://cymon.io and it parse out usefull information. 
Also, the project validate information at https://www.virustotal.com and store the information by MongoDB.

REPOSITORY: https://github.com/giangm9/CymonCrawler


INSTALLATION
-----------
Step 1: Open Command Promt
Step 2: write "python setup.py install"

DESCRIBE
--------
- CymonCrawler.py import DailyCrawler.py. DailyCrawler.py auto crawl and validate daily all usefull information from https://cymon.io.
- AVcrawler.py crawl daily all usefull information from https://otx.alienvault.com/browse.
- Database: 
#===============================================================================
# db : cymon
# collection : addresses
# 
# address : ''
# address_type : ip/domain
# detections : []
#     {   
#         detected :
#         attempts :
#         time :
#         detect_type : 'url/hash'
#         value : 
#     }
#===============================================================================

GUIDE
-----
- AVcrawler.py: class "crawl" information from https://otx.alienvault.com/browse and store it on database.
- CymonCrawler.py: class "crawl" information from https://cymon.io.
		   class "getCymonPage" get some url, day, ... to support crawling.
- DBHelper.py: class "updateAddress" to store information.
	       class "getAddresses" to get information.
- DailyCrawler.py: class "crawl" to crawl daily

TESTS
-----

MAINTAINERS
-----------

- Nguyen Minh Giang - gmail: giangnm95@gmail.com
- Le Truong Giang - gmail: giangm9@gmail.com
- Nguyen Tuanh Anh - gmail: inferno.fire.548@gmail.com
