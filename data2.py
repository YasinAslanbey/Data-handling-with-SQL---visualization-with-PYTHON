# -*- coding: utf-8 -*-
"""Data2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Q8N0e1rq8LNiA1WURbTxs-eTWo94AZyQ
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

!pip install Tensorflow_decision_forests

import tensorflow as tf
import tensorflow_decision_forests as tfdf

import seaborn as sns

Big_dat = pd.read_csv('/content/Yasindata.csv')

Big_dat

Big_dat.head()

Big_dat.info()

Big_dat.describe()

Destin_DAT = pd.read_csv('/content/Destination.csv')
Home_DAT = pd.read_csv('/content/Homeplanet.csv')
VIP_DAT = pd.read_csv('/content/VIP.csv')
AGE_DAT = pd.read_csv('/content/age.csv')

Home_DAT.head()

plt.figure(figsize=(15, 6))
plt.bar(AGE_DAT['Age'], AGE_DAT['Transported_a'], color='blue')

plt.title('Age vs Number of Transported Passengers')
plt.xlabel('Age')
plt.ylabel('Number of Transported Passengers')
plt.grid(True)

plt.show()

plt.figure(figsize=(15, 6))
plt.bar(AGE_DAT['Age'], AGE_DAT['Transported_Percentage_per_age'], color='blue')

plt.title('Age vs Number of Transported Passengers')
plt.xlabel('Age')
plt.ylabel('persentage of Transported Passengers')
plt.grid(True)

plt.show()

print(Home_DAT.dtypes)

# checking nulls
print(Home_DAT['HomePlanet'].isnull().sum())

# FILLNA
Home_DAT['HomePlanet'] = Home_DAT['HomePlanet'].fillna('Unknown')

plt.figure(figsize=(15, 6))
plt.bar(Home_DAT['HomePlanet'], Home_DAT['Transported_Percentage_homeplanet'], color='red')

plt.title('Home vs Number of Transported persentage  Passengers')
plt.xlabel('Homeplanet')
plt.ylabel('persentage of Transported Passengers')
plt.grid(True)

plt.show()

plt.figure(figsize=(15, 6))
plt.bar(Home_DAT['HomePlanet'], Home_DAT['Transported_person'], color='red')

plt.title('Home vs Number of Transported Passengers')
plt.xlabel('Homeplanet')
plt.ylabel('number of Transported  Passengers')
plt.grid(True)

plt.show()

print(Big_dat['Cabin'])

print(Big_dat['Cabin'].head(30))

Big_dat.head()

Destin_DAT.head()

VIP_DAT.head()

#dropping unnececary attributes
columns_to_drop = ['Name', 'PassengerId','CryoSleep','Cabin','RoomService','FoodCourt','ShoppingMall','Spa','VRDeck']
Big_dat = Big_dat.drop(columns = columns_to_drop, axis=1)

Big_dat.head()

# filling nan values

#  Homeplanet
Big_dat['HomePlanet'] =Big_dat['HomePlanet'].fillna('Unknown')
#Destination
Big_dat['Destination'] = Big_dat['Destination'].fillna('Unknown')
#Age
Big_dat['Age'] = Big_dat['Age'].fillna('Unknown')
#VIP
Big_dat['VIP'] = Big_dat['VIP'].fillna('Unknown')
#Transported
Big_dat['Transported'] = Big_dat['Transported'].fillna('Unknown')

# checking is there any nan value
print(Big_dat['HomePlanet'].isnull().sum())
print(Big_dat['Destination'].isnull().sum())
print(Big_dat['Age'].isnull().sum())
print(Big_dat['VIP'].isnull().sum())
print(Big_dat['Transported'].isnull().sum())

#df[['Deck', 'Cabin_num', 'side']] = df['Cabin'].str.split('/', expand = True)
#print(df)

