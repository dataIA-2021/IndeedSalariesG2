#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 10:09:33 2022

@author: alexiadeboynes
"""


import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
import streamlit as st








string = "Prediction de salaire g2"
st.set_page_config(page_title=string, page_icon="💰")


df_france = pd.read_csv('departements-france.csv')
df_france.head()
df = pd.read_csv('France_propre_V2.csv')



st.title('Prédiction de salaire 💰')


options = st.multiselect(
     'Quel poste?',
     df['Poste'].unique())

#st.write('You selected:', options)
options2 = st.multiselect(
     'Quelle Département?',
     df['Departement'].unique())


options1 = st.multiselect(
     'Quelle Région?',
     df['Region'].unique())

optionContract = st.multiselect(
     'Type de contrat?',
     df['Typedecontrat'].unique())

labelencoder = LabelEncoder()
df['Typedecontrat']=labelencoder.fit_transform(df['Typedecontrat'])
#print(df['Typedecontrat'])

df['Poste']=labelencoder.fit_transform(df['Poste'])
#print(df['Poste'])

'''

X = df['Poste'].iloc[:,[0]].values
y = df['Salaire'].iloc[:,-1].values
print(y)

X_train, X_test, y_train , y_test = train_test_split(X,y, test_size = 0.3 , random_state =0)

optionContract = st.multiselect(
     'Type de contrat?',
     df['Typedecontrat'].unique())

#exp = st.sidebar.slider("Contract: ", )

reg = LinearRegression()

reg.fit(X_train, y_train)
y_pred = reg.predict([[optionContract]])

st.write('type de contract: ', optionContract)
st.write('Salaire: ', y_pred)

'''