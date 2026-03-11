import pandas as pd

df = pd.read_csv("Datasets/raw_data.csv")
print(df)

print(df.groupby("country")["income"].mean())
print(df.groupby("gender")["income"].max())
print(df.groupby("country")["income"].agg(["mean","max","min"]))
# print(df.groupby("country")["income"].agg(avg_income="mean",max_income="max",min_income="min"))

print(df.groupby("country").agg({
    "income" : "mean",
    "age" : "mean"
}))
print(df.groupby("country").agg(
    max_income=("income", "max"),
    avg_age=("age","mean")
))