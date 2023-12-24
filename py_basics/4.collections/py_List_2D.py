
'''
List inside a list called 2D 

we could have 3D also and so on

How 2D list would look like:

[1,2,3]
[4,5,6]
[7,8,9]

[1,2,3] [4,5,6] [7,8,9]


'''



# now let's create the list

list2d = [ 
    [],
    [],
    []
]

print(list2d) # [[], [], []]

list2d_1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(list2d_1)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(list2d_1[2][2])

# now print each item of the list

for item in list2d_1: # item is again a list
    # now we will again put a loop for item
    
    for i in item:
        print(i)





