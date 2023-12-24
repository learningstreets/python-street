#List:

'''

List allows duplicate values and it done the things over index


Features:
indexed
Ordered
Changeable / mutable
allow duplicate values
''' 

# let's create a list
li1 = list()  # it will create a empty list.
type(li1)
print(li1)
li2 = []  # this will also create a empty list
type(li2)
print(li2)


li=["abc",345,5.42,True,"abc",5]
print(li)  
print(type(li)) # Type would be list
print(li[0]) # Positive indexing
print(li[-6]) # Negatice indexing

'''
Let's look into range about list
'''

fruits= ["apple", "banana","cherry","dates","fig","papaya","mango"]

print(len(fruits))
print(fruits[2:5]) # it will print from 2 index to < 5 index
print(fruits[:4]) # it will print from start index to < 4 index
print(fruits[2:]) # it will print from 2 index to last  index
print(fruits[-4:-1]) # it will print from -4 index to < -1 index



'''
Let's check if any item is present in the list or not
'''

print("apple" in fruits)  # returns true
print("apple" not in fruits)  # returns false


for f in fruits:
    if   ( "apple" == f ):  
        print ("Present")
        


'''
Find the index of perticular item in list
'''

 


for f in  range(len(fruits)-1,-1,-1):
    print(fruits[f])


'''
Append the list
'''

fruits.append("orange") # we can add only one item at a time
print(fruits)


'''
insert value at perticular index
'''

fruits.insert(0,"Watermilon")
print(fruits)


'''
use extend method to concatinate two list
'''

newFruits = ["Muskmilon","Lichi"]
fruits.extend(newFruits) # alternative fruits = fruits + newfruits
print(fruits)  


'''

del fruits[3]  # delete perticular item from list


'''           

#fruits.remove("value")  # removes first appearance of this value




#Python Collections:
#list
#tuple
#set
#dcitionary
#List:-heterogeneous
#1. ordered
#2. changeable / mutable
#3. allow duplicate values
#l1  = ["abc",3456,5.42,True,"abc"]
#print(l1)
#print(type(l1))
#print(l1[0])
#print(l1[2])
#print(l1[-1])
#print(l1[3])
fruits = ["apple","banana","cherry","dates","fig","papaya","pomo","berry","mango"]
#print(len(fruits))
#print(fruits[2:5])
#print(fruits[:4])
#print(fruits[4:])
#print(fruits[-4:-1])
#print(fruits[2:8:2])
#print(fruits[::-1])
#in and not in
#print("apple"  not in fruits)
#for i in fruits:
#    print(i)
#n = len(fruits)
#for i in range(n-1,0,-1):
#    print(i,fruits[i])
#index
#
#print(fruits.index("pomo"))
#Add items in list:
#append
#insert
#fruits.append("orange")
#print(fruits)
#
#fruits.insert(2,"orange")
#print(fruits)
#print(fruits)
#
#fruits[3]="kiwi"
#
#print(fruits)
#l1 = [1,2,4]
#l2 = [54,3,1]
##
##l1.extend(l2)
#l1 = l1+l2
#print(l1)
#remove
#pop
#fruits.remove("apple")
#print(fruits)
#
#fruits.pop(4)
#print(fruits)
#del 
#print(fruits)
#del fruits[3]
#print(fruits)
#clear 
#fruits.clear()
#print(fruits)
#del fruits
#print(fruits)

