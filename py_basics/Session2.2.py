#TEXT File Handling in python
#open filename,mode
#r -read
#w - write 
#a - append
#x - create
#t eg :'r'
#b eg: binary
#close()
#f = open(r"C:\Users\meenakshi.sugumar\OneDrive - Accenture\Desktop\abc.txt",'r')
##print(f.read(10))
##print(f.readlines())
#data = f.readlines()
#print(data[2])
#f.close()
#f = open(r"C:\Users\meenakshi.sugumar\OneDrive - Accenture\Desktop\abc.txt",'r')
#data = f.readlines()
#data.insert(3,"\nappending in the middle\n")
#data = "".join(data)
#f.close()
#f = open(r"C:\Users\meenakshi.sugumar\OneDrive - Accenture\Desktop\abc.txt",'w')
#f.write(data)
#f.close()
#f.write("\nFile handling in python")
#f.close()
#
#f = open("abc.txt",'x')
#f.close()
#import os
##if os.path.exists("abc.txt"):
##    os.remove("abc.txt")
##else:
##    print("The file doenst exist")
#
#
#os.rmdir("abc")
#import shutil
#shutil.rmtree("abc")