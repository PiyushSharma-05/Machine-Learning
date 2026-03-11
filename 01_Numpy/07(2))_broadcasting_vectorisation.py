import numpy as np

#vectorisation
arr = np.array([1,2,3,4,5])
print(arr * 2)
print(arr + 10)

#broadcasting
arr2 = np.array([[1,2,3,4,5], [1,2,3,4,5]])
print(arr + arr2) # this is possible

arr3 = np.array([[3,4,5,6,7], [1,2,3,4,5], [1,2,3,4,5]])
print(arr2 + arr3) # but this isn't becuase of incompatibility