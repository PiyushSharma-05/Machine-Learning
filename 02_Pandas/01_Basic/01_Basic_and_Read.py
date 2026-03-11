import pandas as pd

Info = {
    "name" : ["Piyush", "Ambika", "Anjali"],
    "GPA" : [7, 7.9, 6.8]
}

df = pd.DataFrame(Info)

print(df)

#for google cloud use import gcsfs

# df = pd.read_csv(r"sales_data_sample.csv", encoding="latin1")
# df = pd.read_excel("SampleSuperstore.xlsx")
df = pd.read_json("sample_Data.json")

print(df)
