import pandas as pd

df = pd.read_csv("globalAirQuality.csv")
#columns
print(df[["city","aqi"]])
print(df.index)
print(df.columns)
#rows
print(df.loc[2])
#cells
print(df.loc[0:5, "aqi"]) #end is inclusive in loc
print(df.loc[0:5, ["aqi","city","humidity"]]) 
print(df.iloc[0:6, 2])
print(df.iloc[0:6, 1:4]) #end is exclusive, in iloc pass index not label

print(df.loc[0:4, ["city", "latitude","aqi","o3"]])
print(df.iloc[0:5, 1:6])

print(df.at[0,"aqi"])
print(df.iat[0,11])

#they all create a view, change in it will chnage in the original
# to get rid of this possible error use .copy()
cities = df["city"].copy()
cities[0] = "Mumbai"
print(cities)

#part2
df = pd.read_csv("globalAirQuality.csv")
print(df[df["aqi"] > 120][["city","temperature"]])
print(df[(df["aqi"] > 100) & (df["temperature"] > 30)])

aqi_df = df[(df["aqi"] > 120) & (df["temperature"] > 30)][["city","temperature","aqi"]]
print(aqi_df)
print(aqi_df.iloc[0]) #iloc takes index
print(aqi_df.loc[6]) #loc takes label

#query -> copy

print(df.query("aqi > 100 & temperature > 32")[["city","aqi","temperature","humidity"]])
aqi_val = 100
print(df.query("aqi > @aqi_val & temperature > 32")[["city","aqi","temperature","humidity"]])