import numpy as np

arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr2d)
print(arr2d.sum())
print(np.sum(arr2d))
sum_columns = np.sum(arr2d, axis = 0)
print(sum_columns)
sum_rows = np.sum(arr2d, axis = 1)
print(sum_rows)

print(arr2d[0:2, 1:2]) #end is not taken(end-1)

arr3d = np.array([[[1,2],[3,4],[5,6]],[[7,8],[9,10],[11,12]]]) #2*3*2
print(arr3d, arr3d.shape)
#indexing
print(arr3d[0,1,1])
print(arr3d[1,2,0])
#slicing
print(arr3d[:, 0, :]) #first row of both layers
print(arr3d[:, :, 0]) #first col of both layers
print(arr3d[:, 1:, 0]) #1st col of both layers except 0th element