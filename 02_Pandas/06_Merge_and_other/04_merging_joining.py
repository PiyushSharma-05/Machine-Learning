import pandas as pd

df_customers=pd.DataFrame({
    "CustomerID" : [1,2,3,4,5],
    "Name" : ["Piyush","Ambika","Divya","Aditya","Pragya"]

})

df_orders=pd.DataFrame({
    "CustomerID" : [1,2,6,8,10],
    "Order Amt" : [260,190,300,120,210]
})

# inner,outer,left,right,    cross->m*n rows to get all possible pairs
merged=pd.merge(df_customers,df_orders, on="CustomerID", how="inner")
print(f"inner join : \n{merged}")
merged=pd.merge(df_customers,df_orders, on="CustomerID", how="right")
print(f"right join : \n{merged}")

#concatenation

df_region1=pd.DataFrame({
    "CustomerID" : [1,2],
    "Name" : ["Piyush","Ambika"]
})

df_region2=pd.DataFrame({
    "CustomerID" : [3,4],
    "Name" : ["Piyushhhht","Ambikkaaaaa"]
})

df_concate=pd.concat([df_region1,df_region2], ignore_index=True) # default axis=0 for vertical concate
print(df_concate)
df_concate2=pd.concat([df_region1,df_region2], axis=1 ,ignore_index=True)
print(df_concate2)