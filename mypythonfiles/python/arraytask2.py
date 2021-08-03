from array import *
g=array('i',[])
s=int(input('enter length: '))
for t in range(s):
    f=int(input('enter next value: '))
    g.append(f)
print(g)
#a=array('i',[12,34,56,67,45])
print(len(g))
srt=0
end=len(g)-1
while srt<end:
    g[srt],g[end]=g[end],g[srt]
    srt=srt+1
    end=end-1
for i in g:
    print(i)