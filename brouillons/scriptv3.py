#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 15:51:38 2022

@author: alexiadeboynes
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


if response.ok:
    soup = BeautifulSoup(response.text, 'lxml')


    #divs = soup.findAll ('div', title = '')
    #span1 = soup.find('span', title = '')
    #h2v = soup.findAll('h2', class = 'jobTitle jobTitle-color-purple')
    title = soup.find('h2', title ='')
    nameCompany  = soup.find('span', class_ = 'companyName')
    companyAddress = soup.find('div', class_ = 'companyLocation')
    salary = soup.find('div', class_ = 'salary-snippet' )
    description =  soup.find('li')
    date = soup.find('span', date = '')
    
print("Job: " + title.text,'\n\n',
          "Company Name:" + nameCompany.text ,'\n\n',
          "Ville " + companyAddress.text,'\n\n',
          'salary ' + salary.text,'\n\n',
          'Description ' + description.text, '\n\n',
          'date ' + date.text)