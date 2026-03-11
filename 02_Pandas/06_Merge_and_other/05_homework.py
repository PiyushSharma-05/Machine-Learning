import pandas as pd

df_customers=pd.DataFrame({
    "CustomerID" : [1,2,3],
    "Name" : ["Piyush","Ambika","Divya"]
})
df_transaction=pd.DataFrame({
    "CustomerID" : [1,2,4],
    "Transaction Amt" : [281,280,210]
})

merged=pd.merge(df_customers,df_transaction, on="CustomerID" , how="inner")
print(merged)

df_customers2=pd.DataFrame({
    "CustomerID" : [1,2,3],
    "Name" : ["Piyush","Ambika","Divya"]
})
df_transaction2=pd.DataFrame({
    "CustomerID" : [4,5,6],
    "Transaction Amt" : [281,280,210]
})

concated=pd.concat([df_customers2,df_transaction2], axis=0, ignore_index=True)
print(concated)