# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 11:08:41 2022

@author: Greta
"""

import requests
from bs4 import BeautifulSoup

url = f'https://fr.indeed.com/France-Emplois-data-analyst'

def get_url(position, location):
    """Generate url from position and location"""
    template = 'https://www.indeed.com/jobs?q={}&l={}'
    position = position.replace(' ', '+')
    location = location.replace(' ', '+')
    url = template.format(position, location)
    return url

response = requests.get(url)
soup_ = BeautifulSoup(response.text, "lxml")

if response.ok:
    soup = BeautifulSoup(response.text, 'lxml')


    #divs = soup.findAll ('div', title = '')
    #span1 = soup.find('span', title = '')

    #h2v = soup.findAll('h2', class = 'jobTitle jobTitle-color-purple')

for i in range(10):
    
    try: title = soup.find('h2', title ='').get_text()
    except: 'pas indiqué'
    
    try: compagnyName  = soup.find('span', class_ = 'companyName').get_text()
    except:'pas indiqué'
    
    try: companyAddress = soup.find('div', class_ = 'companyLocation').get_text()
    except: 'pas indiqué'    
    
    try: salary = soup.find('div', class_ = 'salary-snippet' ).get_text()
    except: 'pas indiqué'
    
    try: description =  soup.find('li').get_text()
    except: 'pas indiqué'
    
    try: date = soup.find('span', date = '').get_text()
    except: print('pas indiqué')

    
print(compagnyName)