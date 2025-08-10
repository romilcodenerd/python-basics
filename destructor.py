# What is destructor?
# A destructoir is a special method that runs when the
# object is deleted.
# we use __del() to delete any object
# we use destructor to clean up (like closing files, 
# freeing memory, etc...)

class Employee:

    def __init__(self):
        print("Employee is created")

    #deleting (calling destructor)
    def __del__(self):
        print("Destructor called, Employee deleted")

obj = Employee()
del obj

#Output:

# Employee is created
# Destructor called, Employee deleted