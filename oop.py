#oop in python

# if you have only one parameter than it is called
# default constructors.
# ex: def__init__(self):

# parameterized constructors:
# where you have more parameters than self
# ex: def__init__(self,marks):

# Program:

class Student:
    name= "romil"
    def __init__(self, fullname):
        self.name = fullname
        print("ading a new student in database...")

#creating object:

s1= Student("romil")

print(s1.name) #romil

s2 = Student("arjun")

print(s2.name) #arjun


class Car:
    color = "blue"
    brand = "bmw"

car1 = Car()
print(car1.color)
print(car1.brand)

class Student:
    name= "romil"
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("adding a new student in database...")

s1 = Student("Romil", 97)
print(s1.name, s1.marks ) #Romil

s2 = Student("arjun", 88)
print(s2.name, s2.marks) #arjun

#Output: 

# adding a new student in database...
# Romil 97
# adding a new student in database...
# arjun 88
 

