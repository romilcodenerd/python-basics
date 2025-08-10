#What are the docstrings in Python?

# Python documentation strings (or docstrings) provide
# a convenient way of associating documentation with 
# Python modules, functions, classes, and methods. 
# It's specified in source code that is used, like a
# comment, to document a specific segment of code. 
# Unlike conventional source code comments, the 
# docstring should describe what the function does.

def greet (name):
    """This function greet user"""
    return "Hello" +name

print(greet.__doc__)

#Output: 
# This function greet user