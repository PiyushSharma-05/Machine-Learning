import pandas as pd


data = {
    "name" : ["Piyush","Ambika","anjali","Rahul","Karan","Aman","Arjun"],
    "age" : [20,19,22,34,23,22,21],
    "city" : ["Rewa", "Jabalpur", "Allahabad","AhmedNagar","Satna","Babina","Gwalior"],
    "salary" : [80000,70000,60000,64000,75000,61000,51000],
    "Performance Score" : [85,81,78,71,67,65,67]
}

df=pd.DataFrame(data)
print(df)
#single column
#ascending=false for descending
df.sort_values(by="age", ascending=True, inplace=True)
print(f"data after sorting : \n{df}")
#multiple column
df.sort_values(by=["age","salary","Performance Score"], ascending=[False,True,False], inplace=True)
print(f"data after sorting : \n{df}")

#aggregation
#sum,min,max,mean,std,count
avg_salary=df["salary"].mean()
print(avg_salary)
max_age=df["age"].max()
print(max_age)
min_score=df["Performance Score"].min()
print(min_score)

# grouping in 11th file