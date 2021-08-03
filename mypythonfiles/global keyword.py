# a=10
# def something():
#     a=15
#     b=8
#     print(a)
#     print(b)
#
# something()
# #print(b)
# print(a)

# a=10
# def something():
#     a=15
#     print('in fun',a)
# something()
# print('out fun',a)
# a=10
# def something():
#     print('in fun',a)
# something()
# print('out fun',a)

# a=10
# def something():
#     global a
#     a=15
#     print('in fun',a)
# something()
#print('out fun',a)

a=10
print(id(a))
def something():
    a=9
    x=globals()['a']
    print(id(x))
    print('in fun',a)
    globals()['a']=15
something()
print('out fun',a)






