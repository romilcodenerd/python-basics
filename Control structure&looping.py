#condition structure and control structure 
#(if,if else, ladder)

#conditional statements allows us to make 
#decisions in code based on conditions.

#if
#if else
#if elif-else
#nesed if

#if statement

'''The if statement is used when you want
to do something only if a condition is true.'''

age=18
if age>=18 :
    print("You are eligible for voting")
else :
    print("Sorry, You are not eligible")

z=3
if z % 2 == 0 :
    print("z is divisible by 2")
elif  z % 3 == 0:
    print("z is divisible by 3")
else:
    print("z is neither divisible by 2 or 3")

room = "bathroom"
area = 20.0

#if-elif-else construct for room
if room == "bed" :
    print("slepp.")
elif room == "bathroom":
    print("take the bath.")
else:
    print("ask mom where is your new room?")

    #if-elif-else construct for area
if area > 20.0 :
 print("pretty big place.")
else:
 print("pretty small place!")

#Nested if (multiple if statements)
# when you want to write multiple if statements.

Romil = 41

if Romil > 21 :
    print("Congratulations you are passed in the exam")

    if Romil > 15 :
        print("you are passed")
    else:
        print("you are failed")

 #even/odd

num = int (input("Please enter number"))
if num%2 ==0: 
    print("even number")
else: 
    print("odd number!")

#elif statement

marks = 100

if marks>= 90:
    print("Grade A")
elif marks>=80:
    print("Grade B")
elif marks>=70:
    print("Grade C")
elif marks>=60:
    print("Grade D")
elif marks>=50:
    print("Grade E")
else:
    print("Sorry You are failed in exam")


















#even / odd number

num=int (input("Please enter number:"))
if num%2==0:
    print("Even Number!")
else:
    print("Odd Number!")

#Type casting 

num = int(input("Please enter number : "))

if num>0:
    if num%2==0:
        print(num,"is positive and even number.")
    else:
        print(num,"is positive and odd number.")
else:
    print(num,"is negative number.")