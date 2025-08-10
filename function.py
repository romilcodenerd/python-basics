# What is function?

# A function is a block of code that performs
# a task and runs only when it is called.

# It helps in:

# Reusing code
# Keeping code organized.

# Use def keyword to define function
# Use parentheses () to call the function.

# Program:

def add1 (a,b): #a,b => parameter
    print(f"Addition of {a} and {b} is: ", a+b)

# Call function

add1 (10,20) # => argument

#Output: Addition of 10 and 20 is: 30

# Function with parameters

def add (a,b):
    return a+b

# Call function
result = add (10,20) # 10,20 => argument
print (result)

#Output: 30

# Default arguments:
# If no value is given, the default will be used.

def greet (name="student"):
    print("Hello", name)
greet() 
greet("romil")  

# Output: 

# Hello student
# Hello romil

def add(a,b= 100):
    return a+b

# Call function

result = add (10,20)
print(result) 

#Output: 

# 30

# Keyword arguments:
# You can pass arguments using key-value.

# Call to function

x = 200
y = 300
result= add (x,y)
print(result) 

#Output:

# 500

def student1 (name, age):
    print (name, age)
age = 20
name = "eomil"
student1 (age = 26, name= "romil")
# => order doesn't matter.

#Output: 
# romil 26

def student (name, age):
    print (name, age)
age = 26
name = "romil"
student (age, name) # => order matter.

#Output:

# 26 romil