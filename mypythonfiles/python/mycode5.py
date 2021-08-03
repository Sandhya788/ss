'''#forloop
x=['sandhya',65,2.5]
print(x)# we can use for loop for printing one by one
for i in x:#i refers to one by one in x,it fetches values from list one by one
	print(i)
x='sandhya'
for i in x:
	print(i)
for j in [2,2.5,'sanju']:
	print(j)
for a in range(10):
	print(a)
for b in range(1,11):
	print(b)
for c in range(20,11,-1):
	print(c)
for i in range(1,25):
	if i%5==0:
		continue
	print(i)
#another way
for t in range(1,25):
	if t%5!=0 and t%3!=0:
		print(t,end=" ")
# one more way
for i in range(1,25):
	if i%5==0:
		i=i+1
		#continue
	print(i)'''
cnt=0
for i in range(1,500):
	j=1
	while j*j<=i:
		if j*j==i:
			cnt+=1
		j+=1
	print(i**2)
#print(cnt)