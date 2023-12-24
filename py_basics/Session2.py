#Function
#
#def add(a,b):#a,b is called as parameters
#    c = a+b
#    print(c)
#    
#add(5,10)#arguments
#default parameter arguments
#arbitary arguments
#keyword arguments
#arbitary keyword arguments
#default :
#def my_func(country="India"):
#    return "I am from "+country
#    
#print(my_func("Canada"))
#print(my_func("Norway"))
#print(my_func())
#print(my_func("India"))
    
#arbitary argument (*)
#def add(a,b):
#    c = a+b
#    print(c)
#    
#add(2,4,5)
#def add(*a):
#    c = 0
#    for i in a:
#        c = c+i
#    return c
#
#print(add(5,6))
#print(add(5,6,7))
#print(add(5))   
#   
#def my_func(*kid):
#    print("The last name is "+ kid[1])
#    
#my_func("msk","parr","bob")
#Keyword arguments(kwargs)  
#def empdetails(name,age,empid):
#    print("The name is",name,
#          "\nThe age is",age,
#          "\nThe empid is",empid)
#
#empdetails(empid = 543,name = "msk",age = 22)
#arbitary keyword arguments: (**kwargs)
#def my_func(**name):
#        print("The last name is "+ name["lname"])
#        
#my_func(mname = "bob",fname ="msk",lname = "parr")