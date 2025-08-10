# *args -> Multiple positional arguments
# Use *args when you don't know how many arguments
# will be passed.
# args is just a name, you can use anything, but * is necessary.
# arguments are received as a tuple.

#program:

def total(*nums):
    print(sum (nums))

total (1,2,3,4)

#Output: 10

# **kwargs -> Multiple named arguments.

#Program:

def student_info(**details):
    print(details)

student_info (name="Romil", age=20)

#Output: {'name': 'Romil', 'age': 26} 