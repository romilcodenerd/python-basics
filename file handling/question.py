# Create a new file "practice.txt" using python.
#Add following data in it:
# Hi everyone
# we are learning File I/O
# using java.
# I like programming in java.

with open("practice.txt", "w") as f:
    f.write("Hi everyone\nwe are learning File I/O\n")
    f.write("using Java./n like programming in Java.")

# WAF that replace all occurrences of "Java" with "Python"
# in above file.

with open("practice.txt", "r") as f:
    data = f.read()

new_data = data.replace("Java", "Python")
print(new_data)

with open("practice.txt", "w") as f:
    f.write(new_data)

# Search if the word "learning" exists in the file or not.

word = "xlearning"
with open("practice.txt", "r") as f:
    data = f.read()
    if(data.find(word) != -1):
        print("Found")
    else:
        print("Not Found")

#convrting it to the function.

def check_for_word():
    word = "xlearning"
    with open("practice.txt", "r") as f:
        data = f.read()
    if(data.find(word) != -1):
        print("Found")
    else:
        print("Not Found")
check_for_word()

# WAF to find in which line of the file does the word 
# "learning" occur first.
# print -1 if word not found.


def check_for_word():
    word = "xlearning"
    with open("practice.txt", "r") as f:
        data = f.read()
    if(word in data):
        print("Found")
    else:
        print("Not Found")

def check_for_line():
    word = "pyq"
    data = True
    line_no = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1 

    return -1

print(check_for_line())

# From a file containing numbers separated by comma, 
# print the count of even numbers.

#1st method

with open("practice.txt", "r") as f:
    data = f.read()
    print(data)

    num = ""
    for i in range(len(data)):
        if(data[i] == ","):
            print(int(num))
            num = ""
        else:
            num += data[i]
 
#2nd method

count = 0
with open("practice.txt", "r") as f:
    data = f.read()

    nums = data.split(",")
    for val in nums:
        if(int(val) % 2 == 0):
            count += 1

print(count)
