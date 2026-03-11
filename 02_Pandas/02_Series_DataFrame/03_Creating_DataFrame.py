import pandas as pd
import numpy as np

#by dictionary
Info = {
    "name" : ["Piyush","Ambika","Arjun"],
    "age" : [23,22,25],
    "gpa" : [9,9.1,7.2]
}

df = pd.DataFrame(Info)
#by list
df = pd.DataFrame([["piyush",23],["Ambika",22]], columns= ["name","age"])
#by np_array
np_arr = np.array([[1,2,3],[4,5,6]])
df = pd.DataFrame(np_arr, columns=["a","b","c"])

print(df, type(df))
