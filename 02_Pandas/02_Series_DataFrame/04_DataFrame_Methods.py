import pandas as pd

df1 = pd.read_csv("employee_data.csv")
# df2 = pd.read_csv("employee_data.json")

print(df1)
# print(df2)

print(df1.head()) #first 5
print(df1.tail(2)) #last 2
print(df1.sample()) #any random
print(df1.info())
print(df1.shape) #(row, col)
print(df1.describe())
print(df1.columns)
print(df1.nunique()) #unique things

df = pd.read_csv("globalAirQuality.csv")
print(df.head())