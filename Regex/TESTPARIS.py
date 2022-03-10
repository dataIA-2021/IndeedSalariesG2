# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 15:54:01 2022

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


df = pd.read_csv('Indeed_Salaries_iledefrance.csv')

df['Departement'].replace(to_replace=r'\d[e]|\d\d[e]', value='', regex=True,inplace=True)



Postal = []

for k in df.index:
    Localisation = re.findall(r"\d\d*", df['Departement'][k], re.IGNORECASE)
    print(Localisation)
    if len(Localisation) != 1:
        Postal.append(00)
    else :
        if int(Localisation[0]) > 100:
            Postal.append(math.floor(int(Localisation[0]) / 1000))
        else: Postal.append(int(Localisation[0]))
               
df['Postal'] = pd.Series(Postal)