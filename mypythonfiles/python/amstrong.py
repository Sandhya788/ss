a=int(input('Enter a Number: '))
res=0
while a!=0:
    rem=a%10
    res=res+rem**3
    a=a//10
print(res)
print(371%10)
print(37%10)
print(3%10)