
# prices = [20,30,40]
# discount=5

# final_price=[]
# for price in prices:
#     price=price - (price*discount)/100
#     final_price.append(price)

# print(final_price)

import numpy as np

prices =np.array([20,30,40])
discount=5

final_prices= prices - (prices*discount)/100
print(final_prices)
result1=prices + 2
print(result1)
result2=prices * 2
print(result2)

matrix=np.array([[1,2,3],[4,5,6]])
vector=np.array([5,10,15])
result3=matrix + vector
print(result3)
result3=matrix * vector
print(result3)
#vectorization

# arr1=[1,2,3]
# arr2=[4,5,6]
# result4=[x+y for x,y in zip(arr1,arr2)]
# print(result4)

arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
result=arr1+arr2
print(result)