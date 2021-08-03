# num=int(input("enter a number:"))
# o=len(str(num))
# res=0
# a=num
# while a:
#     rem=a%10
#     res=res+rem**o
#     a=a//10
# if num==res:
#     print('yes')
#print(res)

# lo=int(input("enter"))
# up=int(input("enter"))
# for num in range(lo,up+1):
#     temp=num
#     o=len(str(num))
#     res=0
#     while(temp!=0):
#         rem = temp% 10
#         res=res+rem**o
#         temp=temp//10
#     if num==res:
#         print(num)


# num = int(input("enter:"))
#
# # Changed num variable to string,
# # and calculated the length (number of digits)
# order = len(str(num))
#
# # initialize sum
# sum = 0
#
# # find the sum of the cube of each digit
# temp = num
# while temp > 0:
#    digit = temp % 10
#    sum += digit ** order
#    temp //= 10
#
# # display the result
# if num == sum:
#    print(num,"is an Armstrong number")
# else:
#    print(num,"is not an Armstrong number")

# n=10
# k=int(input('minimum candies:'))
# if k>=1 and k<=5:
#     print("number of candies sold: ",k)
#     print('number of candies available: ',n-k)
# else:
#     print('INVALID INPUT')
#     print('NUMBER OF CANDIES LEFT: ',n)

# a=input('enter sentence: ')
# print('original sen: ',a)
# s=a.split()
# print(s)
# res=len(s)
# print('word counts: ',res)

# i= str(input())
# print(int(i,17))
import keyword
word=input('enter word: ')
key=keyword.kwlist
if word in key:
    print(word,' is a keyword')
else:
    print('not a keyword')
print(key)

# nu1=int(input('enter first value: '))
# nu2=int(input('enter second value: '))
# i=1
# while i<=nu1 and i<=nu2:
#     if nu1%i==0 and nu2%i==0:
#         gcd=i
#     i=i+1
# print(gcd)