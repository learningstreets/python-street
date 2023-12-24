#OOPS--DRY 
#import random
#import os
#print(type(5))
#print(type(4.566))
#print(type("stree"))
#print(type(True))
#print(type(os))
#print(type([1,2,3]))
#print(type(random))
#class Dog:
#    num_of_legs = 4 #class variables
#    num_teeth = 42
#    can_fly = False
#    
#    def bark(self): # Method
#        return "bow bow"
#print(Dog.can_fly)
#object/instance
#golden_retriever = Dog()
#
#
#print(golden_retriever.bark())
#class Method / Functions
#constructor:---initialise the class variables
class Family:
    def __init__(self,fname,lname,age,gender):#instance variables
        self.fname = "bob"
        self.lname = lname
        self.age = age
        self.gender = gender
    def full_name(self):
        return self.fname + " " +self.lname
father = Family("bob","Parr",44,"male")
mother = Family("Lily","Parr",37,"Female")
print(father.fname,father.gender,father.full_name(),mother.full_name())