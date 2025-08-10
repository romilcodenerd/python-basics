#Reflection refers to the ability for code to be able to examine attributes about objects that might be passed as parameters to a function.

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def show(self):
        print("Name:", self.name)
        print("Age:", self.age)

class Child(Student):
    pass

s = Student('Romil', 26)
c = Child("Manish", 23)
s.show()
c.show()

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print("Name:", self.name)
        print("Age:", self.age)

class Child (Student):
    def __init__(self, name, age, num):
        super(). __init__ (name,age)
        self.num = num

    def show (self):
        super().show()
        print("Num:", self.num)

s = Student('Nupur' , 24)
c = Child('Diksha', 23, 35)

s.show()
c.show()