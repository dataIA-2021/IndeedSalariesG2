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

df = pd.read_csv('Indeed_Salaries.csv')

df.head(100)

cdi = []
cdd = []
interim = []
alternant = []
stage = []



for k in df.index:
    if cdi.append(((re.findall(r"CDI",df['Description'][k], re.IGNORECASE)))):
        
        elif cdd.append((len(re.findall(r"INTERIM",df['Description'][k], re.IGNORECASE)))):
            
            elif interim.append((len(re.findall(r"ALTERNANT",df['Description'][k], re.IGNORECASE)))):
    
    elif alternant.append((len(re.findall(r"CDD",df['Description'][k], re.IGNORECASE)))):
    
    elif stage.append((len(re.findall(r"STAGE",df['Description'][k], re.IGNORECASE)))):
    
    else append(NaN)

#print(pd.Series(type_contrat).value_counts())
df['cdi'] = pd.Series(cdi)
df['interim'] = pd.Series(interim)
df['cdd'] = pd.Series(cdd)
df['alternant'] = pd.Series(alternant)
df['stage'] = pd.Series(stage)
df.head()