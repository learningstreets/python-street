[9:29 AM] Vaishnav, Jyoti
#1D Array with list and tuple
v1=np.array([2,4,7,8])
print(v1)print("")
v2=np.array((2,4,6,8,1))
print(v2)
print(type(v2))print("")
v3=np.array([[1],[4],[6]])
print(v3)

[9:32 AM] Vaishnav, Jyoti
#2D Array
m1=np.array([[1,2,3],[4,1,7],[3,1,7],[3,8,1]])
print(m1)print("")
m2=np.array([[1,2,3,2],[4,1,7,6],[3,1,7,8],[3,8,1,1]])
print(m2)print("")
print("Reshape m1 mat")
m3=m1.reshape(3,4)
print(m3)print("")
print("Transposed m1 mat")
print(m3.T)

[9:32 AM] Vaishnav, Jyoti
import numpy as np

[9:37 AM] Vaishnav, Jyoti
print("")
print("Data Type")
print(m3.dtype)print("")
print("shape of m3 ")
print(m3.shape)print("")
print("Total no of elt ")
print(m3.size)

[9:45 AM] Vaishnav, Jyoti
v1=np.arange(10)
print(v1)v2=np.arange(2,10) #inclusion:exclusion
print(v2)v3=np.arange(2,10,2) #inclusion,exclusion,stepValue
print(v3)v3=np.arange(2,20,3) #inclusion,exclusion,stepValue
print(v3)

[9:47 AM] Vaishnav, Jyoti

print(v1)
print("")
print(v1.reshape(5,2))
print("")
print(v3)
print(v3[0])
print(v3[3])
print(v3[0:3]) #inclusion:excls

[9:50 AM] Hussain, Nabhan
Done

[9:55 AM] Vaishnav, Jyoti
v1=np.random.rand(5)
print(v1)v1=np.random.rand(20)
print("")
print(v1)m1=np.random.rand(3,4)
print("")
print(m1)

[9:57 AM] Kanungo, Anshul
done

v1=np.linspace(5,10,5)
print(v1)



v1=np.linspace(1,20,15)
print("")
print(v1)



v2=np.linspace(2,20,20,retstep=True)
print("")
print(v2)


m1=np.zeros([4,3])
print(m1)



m1=np.zeros([4,3],dtype=int)
print("")
print(m1)



m1=np.ones([4,3],dtype=int)
print("")
print(m1)



m2=np.eye(3,dtype=int)
print("")
print(m2)


[10:19 AM] Vaishnav, Jyoti
m1=np.ones((3,4),dtype=bool)
print(m1)print("")
m1=np.zeros((3,4),dtype=bool)
print(m1)

[10:20 AM] Vaishnav, Jyoti
v1=[True,False]
v2=np.random.choice(v1,size=(5,4))
print(v2)

[10:24 AM] Vaishnav, Jyoti
v1=np.array([3,1,7,9,3])
v2=np.add(v1,3)
print(v2)
print("")
v2=np.subtract(v1,3)
print(v2)
v2=np.negative(v2)
print(v2)

[10:26 AM] Vaishnav, Jyoti
v1=np.array((2,6,8,9,1))
print(v1)
print("Max value is",v1.max())
print("Min value is",v1.min())
print("sum value is",v1.sum())
print(np.sqrt(4))

[10:31 AM] Vaishnav, Jyoti
10:50
 like 1

[10:44 AM] Vaishnav, Jyoti
10:55

[11:08 AM] Vaishnav, Jyoti
mv1=np.array((2,4,7,8))
print(v1)
v2=np.append(v1,50)
print(v2)v2=np.append(v1,[50,60,70])
print(v2)

[11:08 AM] Vaishnav, Jyoti
# col-->axis=1
# row-->axis=0
m1=np.array([[2,3,4],[3,4,5],[2,3,6]])
print(m1)
m2=np.append(m1,[[10],[20],[30]],axis=1)
print("")
print(m2)m2=np.append(m1,[[10,20,30]],axis=0)
print("")
print(m2)

[11:08 AM] Vaishnav, Jyoti
m1=np.array([[2,3,4],[3,4,5],[2,3,6]])
print(m1)m2=np.insert(m1,1,[10,20,30],axis=1)
print("")
print(m2)m3=np.insert(m1,1,[10,20,30],axis=0)
print("")
print(m3)

[11:16 AM] Vaishnav, Jyoti
m1=np.array([[1,2,3],[2,3,4],[3,4,5]])
print(m1)m2=np.delete(m1,1,axis=1)
print("")
print(m2)m2=np.delete(m1,1,axis=0)
print("")
print(m2)m2=np.delete(m1,[1,2],axis=0)
print("")
print(m2)

[11:16 AM] Vaishnav, Jyoti
v1=np.array((2,3,4,7,8,1))
v2=np.delete(v1,1) #VactName,indexposition
print(v2)v2=np.delete(v1,[1,2]) #VactName,indexposition
print(v2)

[11:23 AM] Vaishnav, Jyoti
m1=np.array([[1,2,3],[2,3,4],[3,4,5]])
print(m1)
print("")
print(np.sum(m1,axis=0))
print("")
print(np.sum(m1,axis=1))

[11:38 AM] Vaishnav, Jyoti
import pandas as pd

[11:38 AM] Vaishnav, Jyoti
s1=pd.Series() #EMpty Series
print(s1)

[11:38 AM] Vaishnav, Jyoti
s1=pd.Series(np.array((2,3,5,6)))
print(s1)d1={1:"Ranhul",2:"Diya",3:"John"}
s2=pd.Series(d1)
print("")
print(s2)s3=pd.Series(4,index=[1,2,3,4,5,6])
print("")
print(s3)

[11:38 AM] Vaishnav, Jyoti
d1={1:"Ranhul",2:"Diya",3:np.nan}
s2=pd.Series(d1)
print("")
print(s2)
print("")
print(s2.index)print("")
print(s2.dtype)print("")
print(s2.hasnans)print("")
print(s2.shape)print("")
print(s2.size)print("")
print(s2.empty)

[11:51 AM] Vaishnav, Jyoti
p1=pd.DataFrame() #Empty DataFrame
print(p1)

[11:51 AM] Vaishnav, Jyoti
p2=pd.DataFrame([1,2,3,5])
print(p2)p3=pd.DataFrame({"Id":[101,102,103,104],"Name":["Hohn","John","Diya","Rahul"]})
print("")
print(p3)p4=pd.DataFrame({"Id":[101,102,103,104],"Name":["Hohn","John","Diya","Rahul"]},index=['a','b','c','d'])
print("")
print(p4)

[11:51 AM] Vaishnav, Jyoti
l1=[[101,"John"],[102,"David"],[103,"Diya"]]
p3=pd.DataFrame(l1)
print(p3)p3=pd.DataFrame(l1,columns=["Id","Name"])
print("")
print(p3)

[11:57 AM] Vaishnav, Jyoti
l1=[[101,"John"],[102,"David"],[103,"Diya"]]
p3=pd.DataFrame(l1)
print(p3)p3=pd.DataFrame(l1,columns=["Id","Name"])
print("")
print(p3)l2=['Bang',"Del","Hyd"]
p3["Add"]=pd.DataFrame(l2)
print("")
print(p3)del(p3["Add"])
print("")
print(p3)

[12:00 PM] Vaishnav, Jyoti
p4=p3.append({"Id":104,"Name":"John1"},ignore_index=True)
print(p4)

[12:09 PM] Vaishnav, Jyoti
p1=pd.DataFrame(np.random.rand(3,3))
print(p1)print("")
p1=pd.DataFrame(np.random.rand(3,3),index=['a','b','c'],columns=["1stCol","2nCol","3rdCol"])
print(p1)print("")print("Displaying 1stCOl")
print(p1["1stCol"])
#Two Way for Rows
#using loc
#sing iloc
print("")
print("Displaying 1row")
print(p1.loc["a"])print("")
print("Displaying 1row")
print(p1.iloc[0])

[12:24 PM] Vaishnav, Jyoti
ds=pd.read_csv(r"C:\Users\jyoti.vaishnav\Documents\PythonSessionExample\Day3\mtcars.csv")
print(ds)

[12:28 PM] Vaishnav, Jyoti
print(ds.head()) #Display first 5 rows

[12:28 PM] Vaishnav, Jyoti
ds.head(7)

[12:28 PM] Vaishnav, Jyoti
ds.tail() #last 5 rows

[12:28 PM] Vaishnav, Jyoti
ds.tail(8)

[12:30 PM] Vaishnav, Jyoti
#No of rows and Col
ds.shape

[12:32 PM] Vaishnav, Jyoti
#DataType
ds.dtypes

[12:32 PM] Vaishnav, Jyoti
ds.columns

[12:33 PM] Vaishnav, Jyoti
ds.count()

[12:44 PM] Vaishnav, Jyoti
ds1=pd.read_csv(r"C:\Users\jyoti.vaishnav\Documents\PythonSessionExample\Day3\dataNAN.csv")
ds1

[12:44 PM] Vaishnav, Jyoti
ds1.count()

[12:48 PM] Vaishnav, Jyoti
gp=ds1.groupby('Name of Training').count()
print(gp)

[12:55 PM] Vaishnav, Jyoti
df1=pd.DataFrame({'Name':["Rahul","Sabdy","Diya","Rahul","Diya"],"Course":["BE","MCA","BA","BE","BA"]})
print(df1)
print("")
print(df1.duplicated())
print("")
print(df1.drop_duplicates())

