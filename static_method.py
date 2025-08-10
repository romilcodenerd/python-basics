# Static Methods are that don't use 
# the self parameter (work at class level)


class Student:
    def __init__(self, name, marks): 
        self.name = name
        self.marks = marks

    @staticmethod
    def hello():
         print("hello")

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum +=val
            print("hi", self.name, "your avg score is:", sum/3)

s1 = Student("romil un", [99,98,97])
s1.get_avg()

s1.name = "ironman"
s1.get_avg()

