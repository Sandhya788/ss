a=5 #101
b=6 #110 -->these both requires only three bits
'''temp=a
a=b
b=temp
print(a)
print(b)'''

'''# now without using third variable
a=a+b #11---->but 11 requires 4 bits so we are wasting extra one bit so for that reason we can use XOR
b=a-b #5
a=a-b #6
print(a)
print(b)'''

'''#now using XOR
a=a^b # 3
b=a^b # 5
a=a^b # 6
print(a)
print(b)'''

# in easy way in python
a,b=b,a
print(a)
print(b)

