import pandas as pd
import numpy as np

df=pd.read_csv("employees.csv")
# print(df.head(8))
print(df.isnull().sum())

df["Salary"].fillna(df["Salary"].mean())
df["Bonus %"].fillna(df["Bonus %"].median())

# df.replace([np.inf,-np.inf], np.nan, inplace=True)
# df.fillna(df.mean(numeric_only=True), inplace=True)
numeric_cols=df.select_dtypes(include=["number"]).columns
df[numeric_cols].fillna(df[numeric_cols].mean())

df.drop_duplicates(inplace=True)

df["Salary"]=np.where(df["Salary"]< 0 , df["Salary"].mean(), df["Salary"])

salary_mean = df["Salary"].mean()
salary_std = df["Salary"].std()
lower_bound= salary_mean - (3*salary_std)
upper_bound= salary_mean + (3*salary_std)

df = (df["Salary"] >= lower_bound) & (df["Salary"] <= upper_bound )

df.to_csv("Cleaned_employee_details.csv", index=False)
print("Data cleaniing completed")

