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

obj = PurePath ('C:./config.yml')
with open (obj, 'r') as f:
    conf = yaml.safe_load(f)
my = conf['Mysql']
conf['mysql']['user']

# Connection MYSQL
str = f"mysql+pymysql://{my['user']}:{my['password']}@{my['host']}:{my['port']}/{my['database']}"
engine = create_engine(str, echo=False)

#ouverture du fichier csv
data = pd.read_csv("C:.\Indeed_Salaries.csv")

# Enregistrement du dataframe en BDD MYSQL, table Indeed-Salaries
data.to_sql(name='Indeed_Salaries',con=str, if_exists='append', index=False)  
