'''av=5
x=int(input("how many candles u want:"))
i=1
while i<=x:
    if i>av:
        print('out of stock')
        break
    print('candles')
    i=i+1
print('bye')'''
#x=int(input("how many candles u want:"))
'''i=1
while i<=100:
    if i%3==0:
        i += 1
        continue
    print(i)
    i=i+1
print('bye')'''
'''for i in range(1,101):
    if i%3==0 or i%5==0:
        continue
    print(i)
print('bye')'''
'''for i in range(1,101,2):
    print(i,end=" ")'''
'''i=1
while i<=100:
    if i%2!=0:
        print(i)
    i+=1'''
'''i=1
while i<=100:
    if i%2==0:
        pass
    else:
        print(i)
    i+=1'''
'''i=int(input('how many terms? '))
a=0
b=1
#print(a)
#print(b)
c=0
while c<i:
    c=a+b
    a=b
    b=c
    print(c)
    c=c+1'''
l=int(input('enter a number: '))
m=int(input('enter a number: '))
for n in range(l,m+1):
    if n > 1:
        for x in range(2, n):
            if n % x == 0:
                break
        else:
            print(n,'prime')

