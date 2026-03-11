import numpy as np

arr=[2,3,4,5,6,7]
new_arr=np.insert(arr,3, 34)
new2_arr=np.append(arr, [8,9,15])
print(new2_arr)
print(new_arr)
arr2d=np.array([[2,1],
                [3,4]])
print(arr2d)
#axis-> 0 for row , 1 for column , none for flatten
new_arr2=np.insert(arr2d, 1, [9,1],axis=0)
print(new_arr2)

#concatenate
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])

arr3=np.concatenate((arr1,arr2))
print(arr3)
#delete
arr4=np.delete(arr3, 0)
print(arr4)
arr5=np.delete(new_arr2, 1, axis=0)
print(arr5)
