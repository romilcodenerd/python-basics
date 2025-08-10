# What is Array ?

# An Array is a data structure that stores a colection
# of items of the same data type in contiguous memory location.
# This homogeneity distinguishes arrays from python's 
# built in lists which can store in dynamic data types.

# Program:

"""
arr = [12, 344, 5, 6, 7]
for data in arr: 
    print (data)

#Output: 12 344 5 6 7

#sum of all elements

arr = [5,10,15]
total = 0
for i in arr:
    total +=i
print("sum =", total)

#Output: sum = 30

marks= [70,60,55,44,22]
result= sum (marks)
print("total marks:", result)
"""

#Output: total marks: 251

"""
marks= [70,60,55,44,22]
marks.append(77212)
result= sum (marks)
print("total marks:", result)
"""

#Output: total marks: 77463

marks= [70,60,55,44,22]
print(len(marks)) #Output: 5
result= sum (marks)
print("total marks:", result)

#Output: total marks: 251

marks= [70,60,55,44,22]
marks.pop(2)
result= sum (marks)
print("total marks:", result)

#Output: total marks: 196

marks= [70,60,55,44,22]
marks.remove(22)
result= sum (marks)
print("total marks:", result)

#Output: total marks: 229

marks= [70,60,55,44,22]
x= marks.count(22)
result= sum (marks)
print("total marks:", result)
print(x)

#Output: 1

marks= [70,60,55,44,22]
x= marks.index(22)
result= sum (marks)
print("total marks:", result)
print(x)

#Output: 4

marks= [70,60,55,44,22]
x= marks.clear()
result= sum (marks)
print("total marks:", result)
print(x)

#Output: None