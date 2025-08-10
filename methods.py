# Methods

# Methods are functions that belong to objects.
# class is collection of two things: 
# attributes and methods. 

#Program:

class Student:
    college_name = "Red & White"
    name = "anonymous" #class attribute

    def __init__(self, name, marks):
        self.name = name #obj attr > class attr
        self.marks = marks

    def welcome(self):
        print("welcome student,", self.name)

    def get_marks(self):
        return self.marks

s1 = Student("romil", 98)
s1.welcome()
print(s1.get_marks())

#let's practice question?

class Student:
    def __init__(self, name, marks): 
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum +=val
            print("hi", self.name, "your avg score is:", sum/3)

s1 = Student("romil un", [99,98,97])
s1.get_avg()

s1.name = "ironman"
s1.get_avg()