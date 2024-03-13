from bs4 import BeautifulSoup
import requests
from helpers.sgcarmart import *

listingurl = 'https://www.sgcarmart.com/used_cars/info.php?ID=1276567&DL=4457'
listingurl2 = 'https://www.sgcarmart.com/used_cars/info.php?ID=1265139&DL=1032&utm_content=SLeligible'

#https://www.sgcarmart.com/used_cars/info.php?ID=1246987&DL=2976&utm_content=SLeligible


response = requests.get(listingurl)
listing_url = BeautifulSoup(response.text, 'lxml')


year = manufactured_year_retrieval(listing_url)
#type = listing_url.find(class_='row_bg1').find_all('a')[0].text
transmission = transmission_retrieval(listing_url)

type = type_of_vehicle_retrieval(listing_url)

print(year)
print(transmission)
print(type)