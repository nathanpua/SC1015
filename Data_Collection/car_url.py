from bs4 import BeautifulSoup
import requests
from sgcarmart import *

listingurl = 'https://www.sgcarmart.com/used_cars/info.php?ID=1239227&DL=4234&utm_content=SLeligible,BMW,84800,17020,13-Feb-2018,83531,2017,684,Auto,40925,18/04/2024,33947,39526,,39903,1370,1499,1425,1,Luxury'
listingurl2 = 'https://www.sgcarmart.com/used_cars/info.php?ID=1241808&DL=2976&utm_content=SLeligible'
listingurl3 = 'https://www.sgcarmart.com/used_cars/info.php?ID=1289530&DL=1000&GASRC=sgcm'
#https://www.sgcarmart.com/used_cars/info.php?ID=1246987&DL=2976&utm_content=SLeligible


response = requests.get(listingurl2)
listing_url = BeautifulSoup(response.text, 'lxml')


'''year = manufactured_year_retrieval(listing_url)
#type = listing_url.find(class_='row_bg1').find_all('a')[0].text
transmission = transmission_retrieval(listing_url)

type = type_of_vehicle_retrieval(listing_url)'''

power = power_retrieval(listing_url)


print(power)

#print(type)