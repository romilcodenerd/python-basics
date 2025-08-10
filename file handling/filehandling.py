"""
f = open("demo.txt", "r")

data = f.read()
print(data)

line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)

f.close()
"""

#writing to the file

"""
f = open("demo.txt", "w")

f.write(" I want to learn python sir or mam")

f.close()
"""

#append to the file

#f = open("demo.txt", "a")

#f.write("than i will learn django")

#f.close()

# when file does not exist it will create it fior you

# f = open("sample.txt", "w")
#f.close()

# w++
# f = open("demo.txt", "w+")
# print(f.read())
#f.write("abc")
#f.close()

#append a+

f = open("demo.txt", "a+")
print(f.read())
f.write("abc")
f.close()

