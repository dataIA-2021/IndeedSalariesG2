# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 14:31:36 2022

@author: kylli
"""
import http.client

conn = http.client.HTTPSConnection("indeed-indeed.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "indeed-indeed.p.rapidapi.com",
    'x-rapidapi-key': "46a17314e8mshc034b16c4f70634p1b2bb8jsn3eb43fdc645c"
    }

conn.request("GET", "/apisearch?publisher=undefined&v=2&format=json&callback=%3CREQUIRED%3E&q=java&l=austin%2C%20tx&sort=%3CREQUIRED%3E&radius=25&st=%3CREQUIRED%3E&jt=%3CREQUIRED%3E&start=%3CREQUIRED%3E&limit=%3CREQUIRED%3E&fromage=%3CREQUIRED%3E&highlight=%3CREQUIRED%3E&filter=%3CREQUIRED%3E&latlong=%3CREQUIRED%3E&co=%3CREQUIRED%3E&chnl=%3CREQUIRED%3E&userip=%3CREQUIRED%3E&useragent=%3CREQUIRED%3E", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
#%%
import requests

url = "https://indeed-indeed.p.rapidapi.com/apisearch"

querystring = {"publisher":"undefined","v":"2","format":"json","callback":"<REQUIRED>","q":"java","l":"austin, tx","sort":"<REQUIRED>","radius":"25","st":"<REQUIRED>","jt":"<REQUIRED>","start":"<REQUIRED>","limit":"<REQUIRED>","fromage":"<REQUIRED>","highlight":"<REQUIRED>","filter":"<REQUIRED>","latlong":"<REQUIRED>","co":"<REQUIRED>","chnl":"<REQUIRED>","userip":"<REQUIRED>","useragent":"<REQUIRED>"}

headers = {
    'x-rapidapi-host': "indeed-indeed.p.rapidapi.com",
    'x-rapidapi-key': "46a17314e8mshc034b16c4f70634p1b2bb8jsn3eb43fdc645c"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

#%%
import urllib3
URL = "https://fr.indeed.com/jobs?q=Data&l=Centre-Val+de+Loire"
r = http.request('GET', URL)
script = r.data

#%%
from bs4 import BeautifulSoup
soup = BeautifulSoup(r.read(), 'html.parser')

results = soup.find_all('div', attrs={'data-tn-component': 'organicJob'})

for x in results:
    company = x.find('span', attrs={"itemprop":"name"})
    print ('company:', company.text.strip())

    job = x.find('a', attrs={'data-tn-element': "jobTitle"})
    print ('job:', job.text.strip())

    salary = x.find('nobr')
    if salary:
        print ('salary:', salary.text.strip())

    print ('----------')