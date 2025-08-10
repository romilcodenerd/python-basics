#Use the switch statement to select 
#one of many code blocks to be executed.
#The expression is evaluated once the 
#value of the switch expression is 
#compared once.

num1=int(input("Enter your first number:"))
num2=int(input("Enter your second number:"))

opt= input ("Enter operator:")

match opt:
    case "+":
        print ("Add: ", num1+num2)

    case "-":
        print("Sub: ", num1-num2)

    case "*":
        print("Mul: ", num1*num2)

    case "/":
        print("Div: ", num1/num2)

    case "%":
        print("Rem:", num1%num2)

    case _:
        print("Please enter valid operator")

#Output: Enter your first number:2
#Enter your second number:3
#Enter operator:+
#Add:5