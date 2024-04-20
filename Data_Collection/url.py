import requests
from bs4 import BeautifulSoup

# URL to Scrape from
#https://www.sgcarmart.com/used_cars/listing.php?RPG=20&VEH=1&AVL=2&ORD=
url = 'https://www.sgcarmart.com/used_cars/listing.php?VEH=0&RPG=20&AVL=2'


base_url = 'https://www.sgcarmart.com/used_cars/'

content = requests.get(url)

soup = BeautifulSoup(content.text,'html.parser')
links = soup.find_all('a')
listing_urls = []


for link in links:
    suffix = link.get('href')

    if ('ID=' in suffix) and ('DL=' in suffix):
        listing_url = base_url + suffix
        listing_urls.append(listing_url)



for listing_url in listing_urls:
    print(listing_url)