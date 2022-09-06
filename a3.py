# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 21:53:16 2022

@author: Shilpa
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import os

# print(os.chdir("D:\Lectures\Lectures\Data Science\datasetDS"))

# reading data
automobile = pd.read_csv('Automobile_data.csv')
print(automobile.head())

# # # getting datatypes
print(automobile.dtypes)

#getting statistics
print(automobile.describe())

#cleaning data
print(automobile.isnull().sum())

# # #cleaning the normalized data
# # # Find out number of records having '?' value for normalized losses
print(automobile['normalized-losses'].loc[automobile['normalized-losses'] == '?'].count())
# # #setting missing to mean
# # # Setting the missing value to mean of normalized losses and conver the datatype to integer
nl = automobile['normalized-losses'].loc[automobile['normalized-losses'] != '?']
nlmean = nl.astype(str).astype(int).mean()
automobile['normalized-losses'] = automobile['normalized-losses'].replace('?',nlmean).astype(int)
print(automobile['normalized-losses'].head())



# #cleaning price data
# # Find out the number of values which are not numeric
print(automobile['price'].str.isnumeric().value_counts())


# #List out the values which are not numeric
print(automobile['price'].loc[automobile['price'].str.isnumeric() == False])

# #Setting the missing value to mean of price and convert the datatype to integer
price = automobile['price'].loc[automobile['price'] != '?']
pmean = price.astype(str).astype(int).mean()
automobile['price'] = automobile['price'].replace('?',pmean).astype(int)
print(automobile['price'].head())




# #Checking the numberic and replacing with mean value and conver the datatype to integer
automobile['horsepower'].str.isnumeric().value_counts()
horsepower = automobile['horsepower'].loc[automobile['horsepower'] != '?']
hpmean = horsepower.astype(str).astype(int).mean()
automobile['horsepower'] = automobile['horsepower'].replace('?',pmean).astype(int)




# #Checking the outlier of horsepower

print(automobile.loc[automobile['horsepower'] > 10000])


# #Excluding the outlier data for horsepower
print(automobile[np.abs(automobile.horsepower - automobile.horsepower.mean()) <= (3*automobile.horsepower.std())])


# #Find out the number of invalid value
print(automobile['bore'].loc[automobile['bore'] == '?'])



# #Replace the non-numeric value to null and conver the datatype
automobile['bore'] = pd.to_numeric(automobile['bore'],errors='coerce')
print(automobile.dtypes)


# #Replace the non-number value to null and convert the datatype
automobile['stroke'] = pd.to_numeric(automobile['stroke'],errors='coerce')
print(automobile.dtypes)


# #Convert the non-numeric data to null and convert the datatype
automobile['peak-rpm'] = pd.to_numeric(automobile['peak-rpm'],errors='coerce')
print(automobile.dtypes)

# #remove the records which are having the value '?'
automobile['num-of-doors'].loc[automobile['num-of-doors'] == '?']
automobile = automobile[automobile['num-of-doors'] != '?']
automobile['num-of-doors'].loc[automobile['num-of-doors'] == '?']


# automobile.make.value_counts().nlargest(10).plot(kind='bar', figsize=(15,5))
# plt.title('Number of vehicles by make')
# plt.ylabel('Number of vehicles')
# plt.xlabel('Make');

automobile.symboling.hist(bins=6,color='green');
plt.title("Insurance risk ratings of vehicles")
plt.ylabel('Number of vehicles')
plt.xlabel('Risk rating');

automobile['normalized-losses'].hist(bins=5,color='orange');
plt.title("Normalized losses of vehicles")
plt.ylabel('Number of vehicles')
plt.xlabel('Normalized losses');


automobile['fuel-type'].value_counts().plot(kind='bar',color='purple')
plt.title("Fuel type frequence diagram")
plt.ylabel('Number of vehicles')
plt.xlabel('Fuel type');

automobile['aspiration'].value_counts().plot.pie(figsize=(6, 6), autopct='%.2f')
plt.title("Fuel type pie diagram")
plt.ylabel('Number of vehicles')
plt.xlabel('Fuel type');


automobile.horsepower[np.abs(automobile.horsepower-automobile.horsepower.mean())<=(3*automobile.horsepower.std())].hist(bins=5,color='red');
plt.title("Horse power histogram")
plt.ylabel('Number of vehicles')
plt.xlabel('Horse power');

automobile['num-of-doors'].value_counts().plot(kind='bar',color='purple')
plt.title("Number of doors frequency diagram")
plt.ylabel('Number of vehicles')
plt.xlabel('Number of doors');

