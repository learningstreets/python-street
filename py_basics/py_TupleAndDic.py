#Tuples:
#ordered
#unchangeable/immutable
#duplicates are allowed
#()
#
#t1 = ("apple","banana","cherry","dates")
#
#print(t1)
#print(len(t1))
#print(t1[0])
#x = t1.index("cherry")
#print(x)
#t1.append("bow")
#print(t1[3])
#t1[1]="dog"
#l1 = list(t1)
#print(l1)
#l1.append("ball")
#t1 = tuple(l1)
#print(t1)
#
#t1 = ()
#print(t1,type(t1))
#
#t1 =(5,)
#t2 = (5.678,)
#t3 = ("apple",)
#t4 = (True,)
#t5 = ([1,2,3],)
##
#print(type(t1))
#print(type(t2))
#print(type(t3))
#print(type(t4))
#print(type(t5))
#a = 5,4,6,7
#print(type(a))
#t1 = (1,2,3)
#t2 =(5,4,3)
#t1 = t1+t2
#print(t3)
#Dictionary
#key:value pair
#unordered
#changeable
#does not allow duplicates in keys, but allow duplicats in values:
d1 = {"brand":"Ford","one":1,"Two":3.45,"year":1920}
#print(d1)
#[] , get
#print(d1["brand"])
#print(d1.get("one"))
#
#print(d1.keys())
#print(d1.values())
#print(d1.items())
#for i in d1:
#    print(i)
#for i in d1.keys():
#    print(i)
#for i in d1.values():
#    print(i)
#for i,q in d1.items():
#    print(i,q)
#d1 ={"name":"bob","city":"bangalore","empid":5432}
#
#d1["dept"] = "Admin"
#d1["city"] = "chennai"
#
#print(d1)
#cars_dict = {"Ford":["Figo","Ecosport"],"Honda":"city","Maruti":["Ciaz","Baleno"]}
#
#supercars = {"Ford":"Mustang","Bugatti":"veyron"}
#
#cars_dict.update(supercars)
#print(cars_dict)
#zip
#cars1 = ["Maruti","Honda","Hyundai","Ford"]
#models = [["Baleno","Ciaz"],"City","Figo","Polo"]
#
#cars_dict = dict(zip(cars1,models))
#
#print(cars_dict)