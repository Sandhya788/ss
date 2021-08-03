from array import *
'''arr=array('i',[])
n=int(input("enter the length of arr: "))
for i in range(n):
    x = int(input("enter the next value: "))
    arr.append(x)
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]<arr[j]:
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
    print(arr[i])'''
'''arr=array('i',[])
n=int(input("enter the length of arr: "))
for i in range(n):
    x = int(input("enter the next value: "))
    arr.append(x)
print(arr)
val=int(input("enter thevalue to search : "))
k=0
for e in arr:
    if e==val:
        print(k)
        break
    k+=1'''#this is better
arr=array('i',[])
n=int(input("enter the length of arr: "))
for i in range(n):
    x = int(input("enter the next value: "))
    arr.append(x)
print(arr)
val=int(input("enter thevalue to search : "))
print(arr.index(val))