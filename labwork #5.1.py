# Q.1

class Romil:
 def __init__(self,name,age):
    self.name = name
    self.age = age
    
 def show(self):
        print("Name:", self.name)
        print("Age:", self.age)
        
st1 = Romil ("Nupur", 23)
st2 = Romil ("Diksha", 22)

st1.show()
st2.show()

print(st1.name)
print(st2.name)

# Q.2

class Counter:
    def __init__(self):
        self.count = 0 

    def increment(self):
        self.count += 1 

    def display(self):
        print("Current count:", self.count) 

c = Counter()
c.display()   

c.increment()
c.increment()
c.display()    

# Q.3

""" In Python, self refers to the instance of the class and is required as the  first parameter in instance methods. If you omit self, Python will treat the method as a regular function and will not automatically pass the instance as an argument, which leads to a TypeError when you call the method on an object. """

"""class MyClass:
    def greet():
        print("Hello!")

obj = MyClass()
obj.greet()"""

# Error: TypeError: greet()

# Q.4

class Book:
    def __init__(self, title):
        self.title = title
        
    def show(self, author):
        print(f"Book Title: {self.title}")
        print(f"Author: {author}")

    def set(self, new_title):
        self.title = new_title

# Create object
aa = Book("Harry Potter")

# Show info
aa.show("Romil")

# Change the title
aa.set("Percy Jackson")
aa.show("Rick Riordan")

