
#Inheritance
#single
#multiple
#multilevel
class Person:#base class/Parent class
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
class Teacher(Person):#child class/derived class
    def __init__(self,name,age,gender,grade,subjects = None):
        Person.__init__(self,name,age,gender)
#        super().__init__(name,age,gender)
        self.grade = grade
        self.subjects = []
    def add_subjects(self,new_subject):
        if new_subject not in self.subjects:
            self.subjects.append(new_subject)
        else:
            print("The subject already exists")
    def remove_subjects(self,old_subject):
        if old_subject in self.subjects:
            self.subjects.remove(old_subject)
        else:
            print("The subject doenst exist")
#t1 = Teacher("Lily",22,"female",10)
#
#t1.add_subjects("maths")
#t1.add_subjects("english")
#
#print(t1.name,t1.age,t1.gender,t1.subjects)
class Student(Person):
    def __init__(self,name,age,gender,grade,school_fee):
        super().__init__(name,age,gender)
        self.grade = grade
        self.school_fee = school_fee
    def increase_fee(self):
        self.school_fee =  self.school_fee+1500
        return self.school_fee
#s1 = Student("viv",12,"male",5,10000)
#
#print(s1.age,s1.name,s1.increase_fee(),s1.school_fee)
class Alumni(Student):
    def __init__(self,name,age,gender,grade,school_fee,grad_year):
        super().__init__(name,age,gender,grade,school_fee)
        self.grad_year = grad_year
a1 = Alumni("bob",22,"male",12,10000,2021)
print(a1.age,a1.name,a1.school_fee,a1.grad_year)