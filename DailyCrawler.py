import CymonCrawler
import VirusTotalValidater
import AVcrawler
import datetime


def crawl(delta_time=1):
#     cymondelta = min(4, 1 + delta_time)
#     CymonCrawler.crawl(range(1,), ['malware'], ['ip', 'domain'])
    
    today = datetime.datetime.today().strftime("%Y-%m-%d")
    AVcrawler.crawl(today)
    
    VirusTotalValidater.validateAll()
    
crawl()
