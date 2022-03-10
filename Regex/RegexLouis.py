# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 15:52:07 2022

@author: Greta
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import time
import re
import math
import plotly.express as px
from wordcloud import WordCloud
from collections import Counter



df = pd.read_csv('Indeed_Salaries.csv')
df.rename(columns={"Type de Contrat": "Contrat"}, inplace = True)

df['Contrat'].fillna('CDI',inplace=True)

TContrat = []

for k in df.index:
    Type=re.findall(r"CDI|CDD|Intérim", df['Contrat'][k], re.IGNORECASE)
    try: TContrat.append(Type[0])
    except: TContrat.append('CDI')
    
df['TContrat'] = pd.Series(TContrat)

# ------------------------------------------------------------------------------

# CLEANING LOCALISATION


df['Departement'].replace(to_replace=r'\d[e]|\d\d[e]', value='', regex=True,inplace=True)


Postal = []

for k in df.index:
    Localisation = re.findall(r"\d\d*", df['Localisation'][k], re.IGNORECASE)
    if len(Localisation) != 1:
        Postal.append(00)
    else :
        if int(Localisation[0]) > 100:
            Postal.append(math.floor(int(Localisation[0]) / 1000))
        else: Postal.append(int(Localisation[0]))
               
df['Postal'] = pd.Series(Postal)


<<<<<<< HEAD
# ------------------------------------------------------------------------------

Poste = []


for k in df.index:
    PosteDescription =re.findall(r"DATA", df['Poste'][k], re.IGNORECASE)
    try: Poste.append(PosteDescription[0])
    except: Poste.append('CDI')
    
df['TypePoste'] = pd.Series(Poste)









=======
# CLEANING EN AMONT DES DONNEES
>>>>>>> 0af84859f7863daf530bfc1c0a902d41e7b56d91

# for column in df.columns:
#     df['Poste']=df['Poste'].str.replace('H/F', "")
#     df['Poste']=df['Poste'].str.replace('h/f', "")
#     df['Poste']=df['Poste'].str.replace('("")',"")
#     df['Poste']=df['Poste'].str.replace('F/H', "")
#     df['Poste']=df['Poste'].str.replace('f/h', "")
#     df['Poste']=df['Poste'].str.replace('(F/M/X)', "")
#     df['Poste']=df['Poste'].str.replace('(de)', "")
#     df['Poste']=df['Poste'].str.replace(')', "")
#     df['Poste']=df['Poste'].str.replace('(', "")
#     df['Poste']=df['Poste'].str.replace('(-)', "")
    
df['Poste'] = df['Poste'].str.upper()

PosteDescrip = []

<<<<<<< HEAD
=======
for k in df.index:
    if re.findall(r"INGENIEUR|ENGINEER", df['Poste'][k], re.IGNORECASE):
        PosteDescrip.append('DATA INGENIEUR')
    elif re.findall(r"ENGINEER", df['Poste'][k], re.IGNORECASE):
        PosteDescrip.append('DATA INGENIEUR')
    elif re.findall(r"MANA|MASTER|PROJET", df['Poste'][k], re.IGNORECASE):
        PosteDescrip.append('DATA MANAGER')
    elif re.findall(r"SCIENTIST", df['Poste'][k], re.IGNORECASE):
        PosteDescrip.append('DATA SCIENTIST')
    elif re.findall(r"ARCHITECT", df['Poste'][k], re.IGNORECASE):
        PosteDescrip.append('DATA ARCHITECT')
    elif re.findall(r"DEVELOP", df['Poste'][k], re.IGNORECASE):
        PosteDescrip.append('DEVELOPPEUR')
    elif re.findall(r"BASE", df['Poste'][k], re.IGNORECASE):
        PosteDescrip.append('DATA MANAGER')
    elif re.findall(r"TECH", df['Poste'][k], re.IGNORECASE):
        PosteDescrip.append('TECHNICIEN')
    elif re.findall(r"ANALY", df['Poste'][k], re.IGNORECASE):
        PosteDescrip.append('DATA ANALYSTE')
    elif re.findall(r"CONSUL|BIG", df['Poste'][k], re.IGNORECASE):
        PosteDescrip.append('CONSULTANT')
    elif re.findall(r"MARK", df['Poste'][k], re.IGNORECASE):
        PosteDescrip.append('DATA MARKETING')
    elif re.findall(r"DONN", df['Poste'][k], re.IGNORECASE):
        PosteDescrip.append('GESTIONNAIRE DONNEES')

    else: PosteDescrip.append('0')
    
df['PosteDescrip'] = pd.Series(PosteDescrip)
df.PosteDescrip.value_counts()
>>>>>>> 0af84859f7863daf530bfc1c0a902d41e7b56d91


