import pandas as pd

df_customers = pd.DataFrame({
    "customer_id": [1, 2, 3, 4],
    "name": ["Adam", "Bob", "Charlie", "Dave"]
})

df_orders = pd.DataFrame({
    "order_id": [101, 102, 103, 104],
    "customer_id": [2, 1, 4, 5],
    "amount": [250, 120, 300, 180]
})

merged = pd.merge(df_customers, df_orders, on="customer_id") #inner
merged = pd.merge(df_customers, df_orders,how="left", on="customer_id") #left
merged = pd.merge(df_customers, df_orders,how="right", on="customer_id") #right
merged = pd.merge(df_customers, df_orders,how="outer", on="customer_id") #outer
print(merged)

df1 = pd.DataFrame({
    "id" : [1,2,3],
    "name" : ["Piyush","Ambika","Arjun"]
})
df2 = pd.DataFrame({
    "id" : [4,5,6],
    "name" : ["Adam","Eve","Bob"]
})

df3 = pd.concat([df1, df2]) #row index->0,1,2,0,1,2
df3 = pd.concat([df1, df2], ignore_index=True) #row index->0,1,2,3,4,5
df3 = pd.concat([df1,df2], axis=1) #col
print(df3)