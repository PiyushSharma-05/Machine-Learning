import numpy as np

arr=np.array([2,3,4,5])
print(arr + 2)
print(arr * 5)
print(arr ** 3)

# sum,mean,min,max,std,var

print(arr.sum()) # print(np.sum(arr))
print(np.prod(arr))
print(np.min(arr))
print(np.argmin(arr))
print(np.max(arr))
print(np.argmax(arr))
print(np.mean(arr))
print(np.median(arr))
print(np.std(arr))
print(np.var(arr)) #square of std
print(np.square(arr)) 
print(np.sqrt(arr)) #square root
print(np.log10(arr))
print(np.exp(arr))

print(np.round(3.14)) #rounds off
print(np.ceil(3.14)) #up the number
print(np.floor(3.14)) #down the number
print(np.trunc(3.14)) #cuts decimal

print(np.unique(arr))
print(np.sort(arr))
print(np.abs(arr)) #absolute value