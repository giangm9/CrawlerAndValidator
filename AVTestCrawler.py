from bs4 import BeautifulSoup
import requests

r = requests.get('https://www.av-test.org/en/statistics/spam/')

soup = BeautifulSoup(r.text)

last180 = soup.find('table', {'class': 'avtestreports-spamcountries-top10 table table-striped table-hover table-condensed'})
tbody = last180.find('tbody')

for item in tbody.find_all('tr'):
    country = item.find('td', {'class' : None})
    number = item.find('td', {'class': 'number_cell'})    
    print country.getText().strip() + ":" + number.getText().strip()
    
    
    




