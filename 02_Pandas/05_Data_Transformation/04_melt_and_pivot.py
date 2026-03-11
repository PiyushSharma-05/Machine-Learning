import pandas as pd

df = pd.DataFrame({
    "Country" : ["USA","USA","India","India"],
    "Year" : [2020, 2021, 2020, 2021],
    "Sales" : [100, 120, 90, 110],
    "Profit" : [22, 27, 18, 24]
})

print(df)

#melt(id_vars(KEEP), value_vars(UNPIVOT), var_name(NEW COL NAME), val_name(NEW COL VALUE))
melted_df = df.melt( #wide to long
    id_vars=["Country","Year"],
    value_vars=["Sales","Profit"],
    var_name="metrics",
    value_name="value"
)

print(melted_df)

original = melted_df.pivot( #long to wide
    index=["Country","Year"],
    columns="metrics",
    values="value"
)
print(original)