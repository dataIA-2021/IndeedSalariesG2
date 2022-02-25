#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 06:27:21 2022

@author: alexiadeboynes
"""

import requests
from bs4 import BeautifulSoup

url = f'https://fr.indeed.com/jobs?q=data%20analyst&l=France&vjk=614021636fd3fe48'

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'}

response = requests.get(url,headers=headers)




if response.ok:
    soup = BeautifulSoup(response.text, 'lxml')
    #divs = soup.findAll ('div', title = '')
    #span1 = soup.find('span', title = '')
    #h2v = soup.findAll('h2', class_ = 'jobTitle jobTitle-color-purple')
    h2vv = soup.findAll('span', class_ = 'jobTitle ')
    print(h2vv)
    #print(len(span1))
    #print(span1.text)
    #print(len(h2vv))
 
  #  [print(h2) for  h2 in h2vv]

 print("Joke: " + h2vv.text)