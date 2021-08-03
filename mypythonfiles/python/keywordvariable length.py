def person(name,**data):#single star does not accept keyword agr for accessing we need to give double stars(**)
    print(name)
    for i,j in data.items():
        print(i,":",j)

person('navin',age=28,city='mumbai',mob=9876543210)