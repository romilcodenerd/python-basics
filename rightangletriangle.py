# Nested Loop:

for row in range (1,6):
    for col in range (1, row +1):
        print(col, end= "")
    print()

#Output:
#1
#12
#123
#1234
#12345

#opposite triangle

for row in range (1,6):
 for col in range (5, 5- row, -1):
  print(col, end= '')
 print()

#Output:
#5
#54
#543
#5432
#54321