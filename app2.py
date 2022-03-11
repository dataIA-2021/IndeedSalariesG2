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
import pickle

df = pd.read_csv('df_final.csv')
df_france = pd.read_csv('departements-france.csv')


st.write("""
<style>
.big-font {
    font-size:32px !important;
    color:#169408
}
</style>
""", unsafe_allow_html=True)






st.markdown(f'<h1 style="color:#169408;font-size:44px;">{"Prédiction de Salaire💰"}</h1>', unsafe_allow_html=True)



options = st.multiselect(
     'Quel poste?',
     df['Poste'].unique())



#st.write('You selected:', options)
options2 = st.multiselect(
     'Quel Département?',
     np.sort(df['Departement'].unique()))




optionContract = st.multiselect(
     'Type de contrat?',
     df['Typedecontrat'].unique())



loaded_model = pickle.load(open('finalized_model.sav', 'rb'))


pred = pd.DataFrame( {'Poste': options,
             'Typedecontrat': optionContract,
             'Departement': options2})







y_pred = loaded_model.predict(pred)
print(y_pred)

st.markdown(f'<h1 style="color:#169408;font-size:32px;">{"Salaire en Euros: "}</h1>', unsafe_allow_html=True)
st.write(round(y_pred[0],0))

st.markdown("![Alt Text](https://media.giphy.com/media/eTrYclI5fuEIzuTo3A/giphy.gif)")






