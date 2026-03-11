import pandas as pd

df = pd.read_csv("raw_data.csv")
print(df)

print(df.dtypes)
df2 = df.copy()

mean_age = df["age"].mean()
df["age"] = df["age"].fillna(mean_age)
print(df)
df3 = df["age"] = df["age"].astype("int64")

print(df3.dtypes)
print(df.dtypes)
print(df)

date_str = "2026-02-05"
print(type(date_str))
date_str = pd.Series(["2026-02-05"])
print(type(date_str)) #<class 'pandas.core.series.Series'>
print(type(date_str.dtype)) #<class 'numpy.dtypes.ObjectDType'>
date_str = pd.Series([pd.to_datetime("2026-02-05")])
print(type(date_str.dtype)) #<class 'numpy.dtypes.DateTime64DType'>

aqi_data = pd.read_csv("globalAirQuality.csv")
print(aqi_data)
print(aqi_data["timestamp"].dtype)
aqi_data["timestamp"] = pd.to_datetime(aqi_data["timestamp"])
print(aqi_data["timestamp"].dtype)

df = pd.read_csv("raw_data.csv")
print(df)

print(df["gender"].str.lower())
print(df["gender"].str.upper())
print(df["gender"].str.capitalize())
print(df["name"].str.split(" "))
print(df["country"].str.contains("india", case=False)) #case false indicates all cases false just search for india in country
# print(df)