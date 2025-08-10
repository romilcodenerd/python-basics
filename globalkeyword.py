# The global keyword is used when you want to modify a 
# variable that exists outside of the current function 
# scope—specifically, a variable defined in the global scope.

# Program:

name = "Romil"

def sayHello():
    global name
    print("Hello " + name)
    name = "Nupur"  # Changing the global variable
    print("Username: " + name)

sayHello() 

#Output: Hello Romil
# Username: Nupur

#Multiple values:

name = "Romil"

def sayHello():
    global name

    username="Diksha" # Local variable
    return name, username

print (sayHello())
print (type (sayHello()))

# Output:
# ('Romil', 'Diksha')
# <class 'tuple'>