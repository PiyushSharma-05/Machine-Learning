import pandas as pd

df = pd.read_csv("Datasets/raw_data.csv")
print(df)

#apply
df["tax"] = df["income"].apply(lambda x : "20%" if x >= 55000 else "10%")
# print(df)
#map
# gender_map = {"Male" : "M", "Female" : "F", "Unknown" : "U"}
# df["gender"] = df["gender"].map(gender_map)
# print(df)
#assign
df = df.assign(new_income = df["income"] * 1.1)
#replace
# df["country"] = df["country"].replace("USA", "United States")
# print(df)
df.columns = ["ID","Name","Age","Country","Gender","Income","Tax","New_Income"]
df = df.rename(columns={"Income":"Salary"})
# df = df.rename(index={1:"First"})
df = df.sort_values("Salary")
# df = df.sort_values("Salary", ascending=False)
sorted_df = df.sort_values(["Salary", "Age"])
print(sorted_df.sort_index())
#reset
print(sorted_df.reset_index())
print(sorted_df.reset_index(drop=True))
#ranking
# sorted_df["ranking"] = sorted_df["Salary"].rank()
sorted_df["ranking"] = sorted_df["Salary"].rank(ascending=False)
#resolving ties
sorted_df["ranking"] = sorted_df["Salary"].rank(ascending=False, method="dense")
print(sorted_df)
sorted_df["ranking"] = sorted_df["Salary"].rank(ascending=False, method="min")
print(sorted_df)
sorted_df["ranking"] = sorted_df["Salary"].rank(ascending=False, method="max")


sorted_df = sorted_df[["ID","Name","Age","Country","Gender","Salary","ranking","Tax","New_Income"]]
print(sorted_df)