import pandas as pd

df = pd.read_csv("Datasets/raw_data.csv")
print(df)

new_order = [val for val in df.columns if val != "id"] + ["id"]
print(new_order)
# print(df[new_order])

df2 = df.copy()
# print(df.isnull())
mean_age = df["age"].mean()
df["age"] = df["age"].fillna(mean_age)
df["country"] = df["country"].ffill()
df["gender"] = df["gender"].ffill()
mean_salary = df["income"].mean()
df["income"] = df["income"].fillna(mean_salary)
df["age"] = df["age"].astype("int64").round()
df = df.drop_duplicates()
df = df.sort_values("income", ascending=False)
df = df.reset_index(drop=True)

print(df)
df.to_csv("cleaned_data.xlxs")