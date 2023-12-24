
#csv File Handling :
#reader()
#writer()
#DictReader()
#DictWriter()
#import csv
#f = open(r"C:\Users\meenakshi.sugumar\OneDrive - Accenture\Desktop\class.csv",'r')
#data = csv.reader(f)
#next(data)
#next(data)
#for i in data:
#    print(i)
#data = list(data)
#print(data[2])
#writer()
#writerow()
#writerows()
#import csv
#f = open(r"C:\Users\meenakshi.sugumar\OneDrive - Accenture\Desktop\class.csv",'w',newline='')
#data = csv.writer(f)
#data.writerow(["Name","Empid","Dept"])
#data.writerows([["msk",123,"IT"],["bob",532,"QA"],["lily",5432,'Admin']])
#f.close()
import csv
f = open(r"C:\Users\meenakshi.sugumar\OneDrive - Accenture\Desktop\class.csv",'w',newline='')
#data = csv.DictReader(f)
#for i in data:
#    print(i["Empid"])
l1 = ["Firstname","Lastname"]
data = csv.DictWriter(f,fieldnames=l1)
data.writeheader()
data.writerow({'Firstname':"Lily","Lastname":"Parr"})
data.writerow({'Firstname':"msk","Lastname":"viv"})
data.writerow({'Firstname':"bob","Lastname":"Peter"})
data.writerow({'Firstname':"john","Lastname":"Bpris"})
f.close()