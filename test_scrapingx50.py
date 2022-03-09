# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 11:30:27 2022

@author: kyllianBD
"""
import csv
from datetime import datetime
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd

#%%
def recup_urls():
    """
    

    Returns
    -------
    links : List
        Liste contenant les liens présents sur les 10 premières pages de la recherche Data, Centre-Val-de-Loire.

    """
    base_url = 'https://fr.indeed.com/emplois?q=Data&l=Centre-Val+de+Loire&sort=date&filter=0'
    home_url = []

    for k in range(0, 91, 10):
        home_url.append(base_url + '&start=' + str(k))

    links = []
    root_url = 'https://fr.indeed.com/viewjob?jk='

    for URL in home_url:
        response = requests.get(URL)    
        card = BeautifulSoup(response.text, 'html.parser').find_all('a')
        for k in card:
            if 'data-jk' in k.attrs:
                if (root_url + (k.attrs['data-jk'])) not in links:
                    links.append(root_url + (k.attrs['data-jk']))
    return(links)

#%%
début = datetime.now()
L = []
N = []


for k in range(50):
    L += recup_urls()
    L = list(dict.fromkeys(L))
    N.append(len(L))
    
fin = datetime.now()

#%%
def scrap_job(link_list):
    """

    Parameters
    ----------
    link_list : list
        Liste de str contenant la liste des liens individuels des différentes offres du site

    Returns
    -------
    df : Pandas.Dataframe
        Dataframe composé des champs Titre, Entreprise, Localisation et Salaire

    """
    titre = []
    entreprise = []
    localisation = []
    salaire = []
    for link in link_list:
        response = requests.get(link)    
        soup = BeautifulSoup(response.text, 'html.parser')
        
        try:titre.append(soup.find('h1').get_text())
        except:titre.append('NA')    
        
        cards = soup.find('div', 'icl-u-xs-mt--xs icl-u-textColor--secondary jobsearch-JobInfoHeader-subtitle jobsearch-DesktopStickyContainer-subtitle')
        try:localisation.append(cards.find_all('div')[13].get_text())
        except:localisation.append('NA')
        
        cards = soup.find_all('a')
        try:entreprise.append(cards[9].get_text())
        except:entreprise.append('NA')
        
        try: salaire.append(soup.find('span', 'icl-u-xs-mr--xs attribute_snippet').get_text())
        except:salaire.append('NA')
    
    Titre = pd.Series(titre)
    Entreprise = pd.Series(entreprise)
    Localisation = pd.Series(localisation)
    Salaire = pd.Series(salaire)
    
    frame = {'Poste': Titre,'Entreprise': Entreprise,'Localisation':Localisation,'Salaire':Salaire}
  
    df = pd.DataFrame(frame)
    return(df)

#%%
df = pd.read_csv('Indeed_Salaries.csv')
#%%
df2 = pd.read_csv('Indeed_Salaries_iledefrance.csv')
df2 = df2[:220]
for k in df2.index : 
    df2.Region[k] = 'Île de France' 

#%%
# import des librairies
import sqlite3

#import mysql.connector
import pymysql
from sqlalchemy import create_engine
from sqlalchemy.sql import text
import yaml
import pandas as pd
# librairie pour lire les slah windows
from pathlib import PurePath

obj = PurePath ('D:\Documents\DevIA\Python\SSH\connect.yml')

with open (obj, 'r') as f:
    conf = yaml.safe_load(f)
my = conf['MYSQL']
conf['MYSQL']['user']

# Connection MYSQL
str = f"mysql+pymysql://{my['user']}:{my['password']}@{my['host']}:{my['port']}/bdd_dubiez"
engine = create_engine(str, echo=False)

print(engine)
#%%

#%%


