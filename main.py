from bs4 import BeautifulSoup
import re

import requests

url = "www.dailymotion.com/playlist/x2uo6s_WarnerBrosPicturesFrance_the-big-bang-theory-vf"


r  = requests.get("http://" +url)

data = r.text

soup = BeautifulSoup(data)


list1=[]
for link in soup.find_all('a'):
    #print(link.get('href'))
    if link.get('href'):
        if "/video/" in link.get('href'):
            #print link.get('href')
            list1.append(link.get('href'))
list2=list(set(list1))
for i in list2:
    print i

#for link in soup.find_all('script'):
#    print(link.get('async'))
#for tag in soup.find_all(True):
#    print(tag.name)
    