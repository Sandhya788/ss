from numpy import *
'''a=array([1,2,3,4,5])
print(a)'''
'''a=array('i',[1,2,3,4,5])
print(a)'''
'''a=array([1,2,3,4,5],int)
print(a)'''
#different ways to create array are
    # - arry()
    # - linspace()
    # - logspace()
    # - arange()
    # - zeros()
    # - ones()
#array()
# a=array([1,2,3,4,5])
# print(a.dtype)

# a=array([1,2,3,4,5.0])
# print(a.dtype)
# print(a)
# print(type(a))

# a=array([1,2,3,4,5.0],int)
# print(a.dtype)
# print(a)
# print(type(a))

# a=array([1,2,3,4,5],float)
# print(a.dtype)
# print(a)
# print(type(a))

#linspace
# a=linspace(0,15,16)#stop value included
# print(a)

# a=linspace(0,15,20)#stop value included
# print(a)

# a=linspace(0,15)#stop value included
# print(a)#defaultly it will take 50 parts

#arange()
# a=arange(1,15,2)
# print(a)

#logspace()
# a=logspace(1,40,5)
# print(a)

# a=logspace(1,40,5)
# print('%.2f' %a[4])

#zeros
# a=zeros(5)
# print(a)

#ones
# a=ones(5)
# print(a)

a=ones(5,int)
print(a)
