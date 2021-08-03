from numpy import *
# arr1=array([
#     [1,2,3,6],
#     [4,5,6,7]
# ])
# m=matrix(arr1)
# print(arr1)
# print(m)

# m=matrix('1,2;3,6;4,5;6,7')
# print(m)
# print(m.ndim)

# m=matrix('1,2,3;6,4,5;1,6,7')
# print(m)
# print(m.ndim)
# print(diagonal(m))
# print(m.min())
# print(m.max())

# m1=matrix('1,2,3;6,4,5;1,6,7')
# m2=matrix('1,2,3;6,8,5;2,6,7')
# print(m1)
# print(m2)
# m3=m1*m2
# print(m3)

# m1=matrix('2,4;5,6')
# m2=matrix('6,5;2,4')
# print(m1)
# print(m2)
# m3=m1*m2
# print(m3)

m1=[[1,2,3],
    [4,5,6],
    [7,8,9]]
m2=[[10,11,12],
    [13,14,15],
    [16,17,18]]
res=[[0,0,0],
    [0,0,0],
    [0,0,0]]
print(res)
for i in range(len(m1)):
    for j in range(len(m2[0])):
        for k in range(len(m2)):
            res[i][j]+=m1[i][k]*m2[k][j]
print(res)
for r in res:
    print(r)



