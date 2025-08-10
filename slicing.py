#Slicing lets you carve out portions of sequences 
#like lists, strings, or tuples—without altering
#the original data.


fruits=["apple", "banana", "cherry", "mango"]
print(fruits [1:3])
print(fruits [:2])
print(fruits [2:])

#Output:
#['banana', 'cherry']
#['apple', 'banana']
#['cherry', 'mango']


#methods:
#append(x) Add item at the end


fruits=["apple", "banana", "cherry", "mango"]
fruits.append("grape")
print(fruits)

#Output:
#['apple', 'banana', 'cherry', 'mango', 'grape']

fruits=["apple", "banana", "cherry", "mango"]
fruits.insert(2, "dragon")
print(fruits)

#output:
#['apple', 'banana', 'dragon', 'cherry', 'mango']


fruits=["apple", "banana", "cherry", "mango"]
fruits.remove("banana")
print(fruits)

#Output:
#['apple', 'cherry', 'mango']


fruits=["apple", "banana", "cherry", "mango"]
fruits.pop(1)
print(fruits)

#Output:
#['apple', 'cherry', 'mango']


numbers=[12,3,5,6,78,89]
numbers.sort()
print(numbers)

#Output:
#[3, 5, 6, 12, 78, 89]


numbers=[12,35,6,789,9989]
numbers.reverse()
print(numbers)

#Output:
#[9989, 789, 6, 35, 12]


numbers=[12,25,6,78,89]
print(len(numbers))
print(numbers.count(35))
print(numbers.index(78))

#Output:
#5
#0
#3


numbers=[12,2344,5,687,77]
fruits=['apple', 'banana', 'cherry', 'dragon']
numbers.extend(fruits)
print(fruits)

#Output:
#['apple', 'banana', 'cherry', 'dragon']


fruits=['apple', 'banana', 'cherry']
x= fruits.index("apple")

#Output:
#['apple', 'banana', 'cherry', 'dragon']


fruits=['apple', 'banana', 'cherry']
x=fruits.count("cherry")
print(x)

#Output:
#1 

fruits=['apple', 'banana', 'cherry']
fruits.clear()
print(fruits)

#Output:
#[]