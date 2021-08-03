from array import *
'''a=array('i',[12,34,56,67,45])
x=int(input('enter index u want to delete: '))
for i in range(len(a)):
    if i==x:
     continue
    print(a[i])'''
a=array('i',[12,34,56,67,45])
x=int(input('enter index u want to delete: '))
for i in range(len(a)):
    if a[i]==x:
     continue
    print(a[i])
