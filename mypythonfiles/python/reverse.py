'''i=int(input('enter a number: '))
res=0
while i!=0:
    rem=i%10
    res=(res*10)+rem
    rem=i//10
    i=rem
print(res)'''
#Another way
'''i=int(input('enter a number: '))
res=0
while i!=0:
    rem=i%10
    res=(res*10)+rem
    i=i//10
print(res)'''
l=[2,3,4,5,6,7,8,9]
print(str(l))
strt,end=3,6
l[strt:end]=l[strt:end][::-1]
print(str(l))
