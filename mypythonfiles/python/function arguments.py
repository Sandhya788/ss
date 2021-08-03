# def add(a,b):#--->a,b are formal arguments
#     c=a+b
#     print(c)
# add(5,6)#--->these are actual arguments
#actual arguments are of two types
#       -positional
#       -keyword
#       -default
#       -variable length


#positional:
# def person(name,age):
#     print(name)
#     print(age)
# person('sandhya',20)

# def person(name,age):
#     print(name)
#     print(age)
# person(age=20,name='sandhya')--->here we are using keywords

#default Arguments:
# def person(name,age=10):
#     print(name)
#     print(age)
# person('sandhya',20)

#variable length arguments
# def sum(a,*b):
#     c=a
#     for i in b:
#         c=c+i
#         print(c)
#     print(c)
#
# sum(5,6,34,70)

def sum(*b):
    c=0
    for i in b:
        c=c+i
        print(c)
    print(c)

sum(5,6,34,78)




















































































