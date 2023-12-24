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