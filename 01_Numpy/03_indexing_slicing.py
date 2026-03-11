import numpy as np

arr=np.array([1,2,3,4,5,6,7,8,9])
idx = [2,3,7,1]
print(arr[idx]) # fancy indexing
print(arr[-2])
print(arr[0:9:2]) #start,end,step , in which end is not taken in arr
print(arr[::-2])
print(arr[:-3])
print(arr[[0,3,7]])
print(arr[arr>=6])

list = [1,2,3,4,5,6,7,8,9]
sub_list = list[1:5]
print(sub_list) #makes a copy hence doesn't changes original list

sub_list[1] = 200
print(sub_list)
print(list)

arr2 = np.array([1,2,3,4,5,6,7,8,9])
sub_arr = arr2[1:5]
print(sub_arr) #makes a view hence changes in original arr 
#to do as per list in array use .copy()
sub_arr = arr2[1:5].copy()


sub_arr[1] = 200
print(sub_arr)
print(arr2)