# Function recuression in python is programming
# technique where a function calls itself to solve 
# problem. This approach is particularly useful for 
# problems that can be broken down into smaller,
# simillar subproblems.

# Program:

def factorial (n):
    """ Base condition for factorial. """
    if n==0 or n==1:
        return 1
    else:
        return n* factorial(n-1)

print(factorial(6))

#Output: 720