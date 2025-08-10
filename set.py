# What is a set?

# A set is a collection of unordered, unindexed, and unique items.

# curly braces {} are used.
# duplicates are not allowed.
# unordered: no index, so you can't use s[0]
# mutable: you can add or remove items.

# program:

nums = {1,2,3,4,4,5}
print(nums)
print(type (nums))

#Output: {1, 2, 3, 4, 5} <class 'set'>

#How to setData for numbers?

listdata = [12, 34, 67, 89, 11]
setData = set (listdata)
print (setData)
print (type (setData))

#Output: {34, 67, 11, 12, 89}

#How to add item?

s = {10,20}
s.add(30)
print(s)

#Output: {10, 20, 30}

#How to remove item?

s = {10,24,40}
s.remove(24)
print(s)

#Output: {10, 40}

#How to remove item with safe to use?

s = {10,20, 45, 59}
s.discard(70) #if item is found it remove the item.
print(s)

#Output: {10, 59, 20, 45}

s = {10,20, 45, 59}
s.discard(20) 
print(s)

#Output: {10, 59, 45} 
#As 20 is founded it removed the item.

#How to remove item?

s = {134,6867,4765,3475}
s.pop()
print(s)

#Output: {3475, 4765, 134}

#How to empty all set?

s = {134,345,66,77,888}
s.clear()
print(s)

#Output: set()

#looping through a set

s = {10 ,20, 40, 50, 60, 23, 56}
for item in s:
    print(item)

#Output: 
#50
#56
#20
#23
#40
#10
#60