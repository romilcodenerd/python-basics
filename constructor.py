# A constructor is a special method used to initialize new
# objects of a class. It is automatically invoked when an
# object of the class is created. It is defined using
# the __init__ method within a class.

class Student:

    #constructor
    def __init__(self,name,age):
        self.name = name
        self.age = age

    #member function
    def show(self):
        print("Name:", self.name)
        print("Age:", self.age)
    
st1 = Student("Romil", 26)
st2 = Student("Nupur", 23)
#st.show()

print(st1.name, st1.age)
print(st2.name, st2.age)

#Output: 
# Romil 26
# Nupur 23
