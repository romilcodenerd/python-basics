#The range() function in Python is like a number 
#factory—it generates a sequence of numbers, which
#is super useful when you're looping through 
#something using a for loop.

for x in range (6):
 print(x)

#Output:0
#1
#2
#3
#4
#5

for ch in "Romil":    
    print (ch)
for num in range (11):
    print(num)
for num in range (1,11,3):
    print(num)

#Output:
#R
#o
#m
#i
#l
#0
#1
#2
#3
#4
#5
#6
#7
#8
#9
#10
#1
#4
#7
#10

for num in range (1,11,1):
    if num == 4:
        break
    print(num)

#Output:
#1
#2
#3


