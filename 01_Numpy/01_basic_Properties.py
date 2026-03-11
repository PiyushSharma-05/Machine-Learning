import numpy as np

arr=np.array([[1,2,3],[2,3.9,8]])
print(arr)
print(np.shape(arr))
print(arr.shape)
print(arr.size)
print(arr.ndim)
print(arr.dtype)
print(arr.astype(int))
print(arr.astype(str))

arr1 = np.array([1,4,6,7,8])
print(arr1, type(arr1), arr1.dtype, arr1.shape)

arr2 = np.array([1,3,5,6,4,"Piyush"])
print(arr2, type(arr2), arr2.dtype, arr2.shape)

arr2D = np.array([[1,3,4],[5,7,8],["Piyush","Aman","Ambika"]])
print(arr2D, arr2D.shape)

complex1 = np.array(2 + 5j)
complex2 = np.array(7 - 2j)

print(complex1+complex2, complex2.dtype)