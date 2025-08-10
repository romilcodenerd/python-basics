# Inheritance means one class can use properities
# and methods of another class. The exiisting class.
# The existing class is called parent (Base), and the
# new class is called child.

# Types of Inheritance:
# a) single
# b) multiple
# c) multi level
# d) hierarchical
# e) hybrid

# a) single 

class Parent:
    def Speak (self):
        print("I am Parent")

class Child (Parent):

    pass

c=Child()
c.Speak()

# Output: I am Parent

# b) multiple

class A:
    def method_a (self):
        print("Method from A")

class B:
    def method_b (self):
        print("Method from B")

class C (A,B):
    def method_c (self):
        print("Method from C")

#create object of class C
obj= C()
obj.method_a()
obj.method_b()
obj.method_c()

#Output:

# Method from A
# Method from B
# Method from C

# c) multilevel 

class Grandparent:
    def who (self):
        print("I am Grandparent")

class Child (Grandparent):
    pass

c = Child()
c.who()

#Output: 

# I am Grandparent

# d) hierachical

# Base class
class Parent:
    def func1(self):
        print("This function is in parent class.")

# Derived class 1
class Child1(Parent):
    def func2(self):
        print("This function is in child 1")

# Derived class 2
class Child2(Parent):
    def func3(self):
        print("This function is in child 2")

object1 = Child1()
object2 = Child2()

object1.func1()
object1.func2()
object2.func1()
object2.func3()

#Output:
# This function is in parent class.
# This function is in child 1
# This function is in parent class.
# This function is in child 2

# e) hybrid 

class School:
    def func1(self):
        print("This function is in school.")

# Derived class 1 (Single Inheritance)
class Student1(School):
    def func2(self):
        print("This function is in student 1.")

# Derived class 2 (Another Single Inheritance)
class Student2(School):
    def func3(self):
        print("This function is in student 2.")

# Derived class 3 (Multiple Inheritance)
class Student3(Student1, School):
    def func4(self):
        print("This function is in student 3.")

# Driver code
obj = Student3()
obj.func1()
obj.func2()

# Output:
# This function is in school.
#This function is in student 1.