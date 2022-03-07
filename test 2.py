# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 16:33:01 2022

@author: Greta
"""

import requests
from bs4 import BeautifulSoup

url = f'https://fr.indeed.com/France-Emplois-data-analyst'

response = requests.get(url)


if response.ok:
    soup = BeautifulSoup(response.text, 'lxml')


    #divs = soup.findAll ('div', title = '')
    #span1 = soup.find('span', title = '')
    #h2v = soup.findAll('h2', class = 'jobTitle jobTitle-color-purple')
    title = soup.find('h2', title ='')
    nameCompany  = soup.find('span',class_ = 'companyName')
    companyAddress = soup.find('div', class_ = 'companyLocation')
    salary = soup.find('div', class_ = 'salary-snippet' )
    description =  soup.find('li')
    date = soup.find('span', date = '')