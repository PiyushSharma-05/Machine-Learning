# part of aggregation

import pandas as pd


data = {
    "name" : ["Piyush","Ambika","anjali","Rahul","Karan","Aman","Raj","Simran","Arjun"],
    "age" : [20,20,22,22,25,25,26,22,29],
    "city" : ["Rewa", "Jabalpur", "Allahabad","AhmedNagar","Satna","Katni","Jhansi","Babina","Gwalior"],
    "salary" : [80000,70000,60000,50000,40000,45000,30000,20000,51000],
    "Performance Score" : [85,81,78,71,67,65,54,45,67]
}

df=pd.DataFrame(data)
group=df.groupby("age")["salary"].sum()  # single grouping
group2=df.groupby(["name","age"])["salary"].mean() # multiple grouping
print(group)
print(group2)