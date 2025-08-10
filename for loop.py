#A for loop in Python is like a choreographer—
#it tells your code to repeat a certain action
#for every item in a collection, elegantly and
#efficiently.


for num in range(1,11):
    print(num)

for num in range (1,11):
    print (num*22)

    print(range (1,11))

    for ch in "Romil":
     print(ch)

for num in range (11):
    print(num)

for num in range (1,11,3):
    print(num) 

for i in range(0):
 print(i) 

 #break

for num in range (1,11,1):
    if num == 4:
        break

    print(num) 

for num in range (1,11,1):
    if num == 3:
        continue
    print(num) 

for num in range (1,11,1):
    if num == 4:
        pass
    print(num)