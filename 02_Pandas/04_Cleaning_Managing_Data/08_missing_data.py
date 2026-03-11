import pandas as pd


data = {
    "name" : ["Piyush","Ambika","anjali","Rahul","Karan","Aditya","Raj","Simran","Arjun"],
    "age" : [20,19,22,34,None,25,26,28,29],
    "city" : ["Rewa", "Jabalpur", "Allahabad","AhmedNagar","Satna","Datiya","Jhansi","Babina","Gwalior"],
    "salary" : [80000,70000,60000,50000,40000,None,30000,20000,51000],
    "Performance Score" : [85,81,78,71,67,None,54,45,67]
}
#checking
df = pd.DataFrame(data)
print(df)
print(df.isnull())
print(df.isnull().sum())

#droping or filling , axis=0->row and 1->column, default row
df.dropna(axis=0,inplace=True)
print(df)


df["age"].fillna(df["age"].mean() , inplace=True)
df["salary"].fillna(df["salary"].mean(), inplace=True)
df["Performance Score"].fillna(df["Performance Score"].mean(), inplace=True)
print(df)

# interpolation 

df.interpolate(method="linear",axis=0, inplace=True)
print(df)
#OR
df["age"]=df["age"].interpolate(method="linear")
df["salary"]=df["salary"].interpolate(method="linear")
df["Performance Score"]=df["Performance Score"].interpolate(method="linear")
print(df)