#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 09:25:21 2022

@author: alexiadeboynes
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression



string = "Prediction de salaire g2"
st.set_page_config(page_title=string, page_icon="💰")

st.title('Prédiction de salaire 💰')



df = pd.read_csv('Indeed_Salaries.csv')

#remove HF
for column in df.columns:
    df['Poste']=df['Poste'].str.replace('H/F', "")
    df['Poste']=df['Poste'].str.replace('h/f', "")
    df['Poste']=df['Poste'].str.replace('("")',"")    
    
#salaire average    

def salary_stripper(dataframe, column):
    dataframe[str(column)] = dataframe[str(column)].replace({'$':''}, regex = True)
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





options = st.multiselect(
     'Quel poste?',
     df['Poste'])

#st.write('You selected:', options)


options1 = st.multiselect(
     'Où',
     df['Localisation'])

#st.write('You selected:', options1)


#st.write('## Le jeux de données')
#st.write(df)






