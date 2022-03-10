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
df.rename(columns={"Type de Contrat": "contrat"}, inplace = True)


def salary_stripper(dataframe, column):
    dataframe[str(column)] = dataframe[str(column)].replace({'\$':''}, regex = True)
    dataframe[str(column)].replace(regex=True,inplace=True,to_replace=r'\D',value=r' ')
    dataframe[str(column)] = dataframe[str(column)].str.replace(' ',',')
    dataframe = dataframe.join(dataframe[str(column)].str.split(',,,', 1, expand=True).rename(columns={0:'Low', 1:'High'}))
    dataframe['Low'] = dataframe['Low'].str.replace(',','')
    dataframe['Low'] = dataframe['Low'].astype('float64')
    dataframe.drop(str(column), axis=1, inplace=True)
    dataframe['High'] = dataframe['High'].str.replace(',','')
    dataframe['High'] = dataframe['High'].apply(pd.to_numeric)
    dataframe['Average'] = dataframe[['Low', 'High']].mean(axis=1)
    return dataframe

df = salary_stripper(df, 'Salaire')



salaire1 = []
for k in df.index:
    salaire1.append(len(re.findall(r"\d\d\.k", df['contrat'][k], re.IGNORECASE)))




# df['moyenne'] = df.mean(axis=1)


# new = df['contrat'].str.split(",", n = 1, expand = True )

# df['Type de Temps']= new[0]
# df['Type contrat']= new[1]


# salaire = []

# for k in df.index:
#         salaire.append((re.findall(r"\d\d\d\d\d", df['contrat'][k], re.IGNORECASE)))

# df['salaire'] = pd.Series(salaire)


















# temp = (len(re.sub('TEMPS', '', df['contrat'], re.IGNORECASE)))
# df['temp'] = pd.Series(temp)

# # temp.append((re.sub(str("Temps plein"), " ", df["contrat"])))
# for k in df.index:
#     temp = re.sub('TEMPS', '', str(temp), re.IGNORECASE)

# df['temp'] = pd.Series(temp)



# # for k in df.index:
# #     typecontrat.append(((re.findall(r"CDI",df['contrat'][k], re.IGNORECASE))))

# # df['typecontrat'] = pd.Series(typecontrat)

# # df.head(10)







