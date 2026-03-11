import pandas as pd

data = {
    "name" : ["Piyush","Ambika","anjali"],
    "age" : [20,19,22],
    "city" : ["Rewa", "Jabalpur", "Allahabad"]
}

df = pd.DataFrame(data)

print(df)

# df.to_csv("Output.csv", index=False)
# df.to_excel("Output.xlsx", index=False)
df.to_json("Output.json", index=False)