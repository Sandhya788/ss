i=int(input('enter a number: '))
t=i
print(t)
res=0
while i!=0:
    rem=i%10
    res=(res*10)+rem
    i=i//10
if t==res:
    print(t,'is a palindrome')
else:
    print(t,'is not a palindrome')