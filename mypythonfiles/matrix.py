from numpy import *
# a=array([
#
#         [1,2,3],
#         [4,5,6]
#     ])
# arr2=a.flatten()
# print(a)
# print(arr2)
# print(a.dtype)
# print(a.ndim)
# print(a.shape)
#print(a.size)

a=array([

        [1,2,3,6,5,2],
        [4,5,6,7,5,3]
    ])
arr=a.flatten()
arr2=arr.reshape(3,4)
arr3=arr.reshape(2,2,3)
print(a)
print(arr)
print(arr2)
print(arr2.ndim)
print(arr3.ndim)