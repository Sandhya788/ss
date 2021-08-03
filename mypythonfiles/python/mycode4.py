#while loop
'''print('thelusko')
print('thelusko')
print('thelusko')
print('thelusko')'''
#for iterating many times we can use loops
'''a=1#-->initialization
while a<=5:#-->condition
	print('Telusko')
	a=a+1#-->increment/decrement
#until condition becomes true'''
'''a=5#-->initialization
while a>=0:#-->condition
	print('Telusko',a)
	a=a-1#-->increment/decrement'''
# while inside while
'''a=1#-->initialization
#j=1
while a<=5:#-->condition
	print('Telusko',end=" ")
	j=1
	while j<=4:
		print('rockers',end=" ")
		j+=1
	print()
	a=a+1#-->increment/decrement
	#print()'''
#1) write code to print all the values from 1 to 100 skip the numbers which are divisible by 3 or 5
a=1
while a<=100:
	if a%3==0:
		a+=1
		#continue
	print(a)
	a+=1
'''b=1
while b<=5:
	print('#',end=" ")
	c=1
	while c<=5:
		print('#',end=" ")
		c+=1
	print()
	b+=1'''
