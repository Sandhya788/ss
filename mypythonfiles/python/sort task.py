from array import *
vals= array('i',[5,9,8,4,2])
for i in range(0,len(vals)):
    for j in range(i+1,len(vals)):
        if vals[i]>vals[j]:
            temp=vals[i]
            vals[i]=vals[j]
            vals[j]=temp
    print(vals[i])
vals= array('i',[5,9,8,4,2])
for i in range(0,len(vals)):
    for j in range(i+1,len(vals)):
        if vals[i]<vals[j]:
            temp=vals[i]
            vals[i]=vals[j]
            vals[j]=temp
    print(vals[i])
