import pandas as pd

print(pd.read_csv('Book1.csv'))

data_csv=pd.read_csv('Book1.csv')

print(data_csv.size)

print(data_csv.head(2))

print(data_csv.tail(2))

print(data_csv.ndim)

print(data_csv.at[2,'course'])
#print(data_csv.iat[1,2])

print(data_csv.columns)
print(data_csv.shape)
print(data_csv.loc[:,'course'])

print(data_csv.head(1))

print(data_csv.size)

print(data_csv.dtypes)
print(data_csv.dtypes.count())
print(data_csv.info())