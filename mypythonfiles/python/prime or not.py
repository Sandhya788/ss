#a=int(input("enter a number: "))
l=int(input("enter a number: "))
u=int(input("enter a number: "))
for x in range(l,u):
    if x>1:
        for i in range(2,x):
            if x%i==0:
                break
        else:
            print(x,'prime')
    else:
        print(x,'not a  prime')