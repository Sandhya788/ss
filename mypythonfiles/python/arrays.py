'''#array is a collection of elements of same type
#import array as arr'''
from array import *
'''vals= array('i',[5,9,8,4,2])
print(vals)'''
'''vals= array('i',[5,9,-8,4,2])
print(vals)'''
'''vals= array('I',[5,9,-8,4,2])
print(vals)'''
'''vals= array('b',[5,9,8,4,2])
print(vals)'''
'''vals= array('i',[5,9,8,4,2])
print(vals.buffer_info())'''#(2395817546576-->address, 5-->size)

'''vals= array('i',[5,9,8,4,2])
print(vals.count(8))'''
'''vals= array('i',[5,9,8,4,2])
print(vals.reverse())'''#it does not work
'''vals= array('i',[5,9,8,4,2])
vals.reverse()
print(vals)'''
'''vals= array('i',[5,9,8,4,2])
for i in range(5):
    print(vals[i])'''
'''vals= array('i',[5,9,8,4,2])
for i in range(len(vals)):# more dynamic
    print(vals[i])'''
'''vals= array('i',[5,9,8,4,2])
for i in vals:
    print(i)'''
'''vals= array('i',[5,9,8,4,2])
for a in range(5):
    print(vals[a])'''
'''char= array('u',['p','q','r','s','t'])
print(char)'''
'''char= array('u',['p','q','r','s','t'])
for i in char:
    print(i)'''
'''char= array('u',['p','q','r','s','t'])
for e in range(5):
    print(char[e])'''
'''char= array('u',['p','q','r','s','t'])
for s in range(len(char)):
    print(char[s])'''
vals= array('i',[5,9,8,4,2])
narr=array(vals.typecode,(a*a for a in vals))
for j in narr:
    print(j)
#print(vals,narr)

'''vals= array('i',[5,9,8,4,2])
narr=array(vals.typecode,(a*a for a in vals))#Accessing from already existing one 
f=0
while f<0:
    print(narr[f])
    f=f+1'''
vals= array('i',[5,9,8,4,2])
narr=array(vals.typecode,(a*a for a in vals))
f=0
while f<len(narr):
    print(narr[f])
    f=f+1


















































































