try:
    num1 = 10
    num2 = 0
    result= num1 | num2
    print(f"result:{result}")

except:
    print("Somethiing wrong!!")

print("Hello python!")


try:
    f = open("data.txt.py", "r")
except ValueError:
    print("please enter a valid number!")
except ZeroDivisionError:
    print("you can't divide by zero!")
except FileNotFoundError:
    print("File Not Found!!")
else:
    print(f.read())