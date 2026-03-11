import numpy as np 

arr=np.array([1,2,np.nan,4,np.nan,6])
print(np.isnan(arr))
print(arr)
cleaned=np.nan_to_num(arr,nan=23)
print(cleaned)

arr2=np.array([1,2,np.inf,4,-np.inf,6])
print(np.isinf(arr2))
cleaned2=np.nan_to_num(arr2, posinf=1000, neginf=-1000)
print(cleaned2)