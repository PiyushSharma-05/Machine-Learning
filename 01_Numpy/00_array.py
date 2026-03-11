import numpy as np

list=[1,2,3,4,5]
print(list)

array=np.array(list)
print(array)

array2d=np.array([[1,2,3],
                 [4,5,6],
                 [7,8,9]])
print(array2d)

# matrix or multid array
matrix1=np.array([[2,4,6],[3,5,1]])
print(matrix1)

array0=np.zeros((3,2))
array0=np.zeros(3)
print(array0)
array1=np.ones(4)
print(array1)
filled_array=np.full((3,2),12)
print(filled_array)

arr = np.arange(1,10,2)
print(arr)

identity_matrix=np.eye(4)
print(identity_matrix)

arr2 = np.linspace(0,50,10)
print(arr2)