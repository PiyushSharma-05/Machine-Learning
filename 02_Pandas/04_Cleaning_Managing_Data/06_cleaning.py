import pandas as pd

df = pd.read_csv("raw_data.csv")
print(df)

print(df.isnull())
print(df.isnull().sum())
print(df.fillna(0))
print(df["age"].fillna(df["age"].mean()))
print(df.dropna()) #rows
print(df.dropna(axis=1)) #cols
print(df.ffill())
print(df.bfill())

cleaned_df = df.copy()
age_mean = cleaned_df["age"].mean()
cleaned_df["age"] = cleaned_df["age"].fillna(age_mean)
income_mean = cleaned_df["income"].mean()
cleaned_df["income"] = cleaned_df["income"].fillna(income_mean)
cleaned_df["gender"] = cleaned_df["gender"].ffill()
cleaned_df["country"] = cleaned_df["country"].ffill()
print(cleaned_df)

#duplicate
print(df.duplicated())
print(df["id"].duplicated())
print(df["name"].duplicated())
df2 = df.copy()
df.drop_duplicates(inplace=True)
print(df)
print(df2)