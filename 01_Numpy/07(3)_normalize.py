import numpy as np

arr1 = np.array([[1,2], [3,4]])
mean = np.mean(arr1)
std = np.std(arr1)
print(mean)
print(std)

normalised_arr = (arr1 - mean)/std
print(normalised_arr) #mean of this arr is 0 and std is 1