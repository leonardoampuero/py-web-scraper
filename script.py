
import requests
import json
import sys
from bs4 import BeautifulSoup

URL = 'https://givingassistant.org/coupon-codes/'

if (len(sys.argv) < 2):
  print ('Argument site is missing')
  sys.exit()

print('Scraping ' + sys.argv[1])
input = sys.argv[1]
page = requests.get(URL + input)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find_all('h3', string='Similar Store Coupons')

if (len(results) == 0):
  print ('Similar Sites not found')
  sys.exit()

sites = results[0].parent.find_all('a')
similarSites = []

for var in sites:
  href = var.get('href')
  splitUrl = href.split('/')
  host = splitUrl[len(splitUrl) - 1 ]
  similarSites.append({ 'name' : var.string, 'url' : var.get('href'), 'host': host}) 

list2 = {
  'input': input,
  'hostnames' : similarSites
}

print(json.dumps(list2, indent=4))
