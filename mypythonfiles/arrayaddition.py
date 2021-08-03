from numpy import *
# a=array([1,2,3,4,5])
# for i in range(len(a)):
#     print(a[i]+5)

# a1=array([1,2,3,4,5])
# a2=array([6,1,9,3,2])
# a1=a1+5
# a2=a2+5
# print(a1,a2)


# a1=array([1,2,3,4,5])
# a2=array([6,1,9,3,2])
# a3=a1+a2#it is also called as vectorized operation
# print(a1,a2)
# print(a3)

# a1=array([1,2,3,4,5])
# print(sum(a1))

# a1=array([1,2,3,4,5])
# print(sin(a1))

# a1=array([1,2,3,4,5])
# print(cos(a1))

# ar=array([1,2,3,4,5])
# print(sqrt(ar))

# ar=array([1,2,3,4,5])
# print(min(ar))

#reversing
# ar=array([1,2,3,4,5])
# str=0
# end=len(ar)-1
# while str<end:
#     ar[str],ar[end]= ar[end],ar[str]
#     str=str+1
#     end-=1
# print(ar)


# ar=array([1,45,96,25,23])
# for i in range(0,len(ar)):
#     for j in range(i+1,len(ar)):
#         if ar[i]<ar[j]:
#             t=ar[i]
#             ar[i]=ar[j]
#             ar[j]=t
#     print(ar[i])

# ar=array([1,45,96,25,23])
# for i in range(0,len(ar)):
#     for j in range(i,len(ar)):
#         if ar[i]<ar[j]:
#             t=ar[i]
#             ar[i]=ar[j]
#             ar[j]=t
#     print(ar[i])

# ar=array([1,45,96,25,23])
# for i in range(0,len(ar)):
#     for j in range(i,len(ar)):
#         if ar[i]>ar[j]:
#             t=ar[i]
#             ar[i]=ar[j]
#             ar[j]=t
#    print(ar[i])

# ar=array([1,45,96,25,23])
# for i in range(0,len(ar)):
#     for j in range(i+1,len(ar)):
#         if ar[i]>ar[j]:
#             t=ar[i]
#             ar[i]=ar[j]
#             ar[j]=t
#     print(ar[i])

# a1=array([1,2,3,4,5])
# a2=array([7,8,9,6,2])
# print(concatenate([a1,a2]))

#copying
# arr=array([1,4,7,2,5])
# arr1=arr
# print(arr)
# print(arr1)
# print(id(arr))
# print(id(arr1))---->this is also known as aliasin

# arr1=array([9,6,3,5,2])
# arr2=arr1.view()#this function is used to create new array in different location
# print(arr1)
# print(arr2)
# print(id(arr1))
# print(id(arr2))

# arr1=array([9,6,3,5,2])
# arr2=arr1.view()#this function is used to create new array in different location
# #Shollow copy
# arr1[1]=7
# print(arr1)
# print(arr2)
# print(id(arr1))
# print(id(arr2))

# arr1=array([9,6,3,5,2])
# arr2=arr1.copy()#this function is used to create new array in different location
# #deep copy
# arr1[1]=7
# print(arr1)
# print(arr2)
# print(id(arr1))
# print(id(arr2))

#adding using for
# a=array([1,2,3,6,1])
# b=array([7,8,9,4,5])
# for i in range(0,len(a)):
#     for j in range(i,len(b)):
#         arr=a[i]+b[j]
#         break
#     print(arr)

#maximum value
# vals= array([5,9,8,4,10])
# for i in range(0,len(vals)):
#     for j in range(0,len(vals)):
#         if vals[i]>vals[j]:
#             vals[j]=vals[i]
# print(vals[j])

