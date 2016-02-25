PROJECT
-------
Construction Crawler from the site to provide resources about the Malicious

INTRODUCTION
------------

Included:
All source files(.py):
- AVcrawler.py			Crawl daily information from https://otx.alienvault.com/browse
- CymonCrawler.py		Crawl daily information from https://cymon.io
- DBHelper.py			Store and get information
- DailyCrawler.py		Call to crawl either AVcrawler.py or CymonCrawler.py or both.		
- VirusTotalValidater.py	Validate information crawled from https://www.virustotal.com.
- setup.py			Install project

This project use python 2.7 and beatifulsoup to crawl information from https://otx.alienvault.com/browse, https://cymon.io and it parse out usefull information. 
Also, the project validate information at https://www.virustotal.com and store the information by MongoDB.

REPOSITORY: https://github.com/giangm9/CymonCrawler


INSTALLATION
------------
Step 1: Install python 2.7, MongoDB, beatifulsoup.
Step 2: Open Command Promt.
Step 3: write "pip install setup.py".

DATABASE DESCRIBER
------------------
#===============================================================================
# db : cymon
# collection : addresses
# 
# address : ''
# address_type : ip/domain
# Array of Embedded Documents:
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
- Sample code: 
>> from CrawlerAndValidator import DailyCrawler
	
>> DailyCrawler.crawl();


MAINTAINERS
-----------

- Nguyen Minh Giang - gmail: giangnm95@gmail.com
- Le Truong Giang - gmail: giangm9@gmail.com
- Nguyen Tuanh Anh - gmail: inferno.fire.548@gmail.com
