# Operations

#union 'set1
#intersection set1 & set2 - common item in both sets.
#difference set1 - set2 - items in set1 but not in set2
#symmetric diff set1 ^ set2 - items in either set but not both
#isSubset set1.issubset (set2) - true if set 1 is part of set2
#issuperset set1.issuperset - true if set1 contains set2.

#program:

a={1,2,3}
b={3,4,5}

print(a|b) #union ->{1, 2, 3, 4, 5}
print(a&b) #intersection ->{3}
print(a-b) #difference ->{1, 2}
print(a^b) # symmetric difference-> {1, 2, 4, 5}

#