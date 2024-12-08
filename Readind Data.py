import pandas as pd

df = pd.read_csv('sales_data.csv')

print(df)

df = pd.read_csv('sales_data.csv', usecols=['sales_id', 'quantity'])

print(df)

df = pd.read_csv('sales_data.csv', skiprows=2)

print(df)

print('hello')
