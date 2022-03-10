

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


# ------------------------------------------------------------------------------

Poste = []


for k in df.index:
    PosteDescription =re.findall(r"DATA", df['Poste'][k], re.IGNORECASE)
    try: Poste.append(PosteDescription[0])
    except: Poste.append('CDI')
    
df['TypePoste'] = pd.Series(Poste)














