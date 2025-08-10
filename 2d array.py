"""
groceries = [["apple", "orange", "banana", "coconut"],
            ["carrots", "celery", "potatoes"],
            ["milk", "cheese", "panner"]]
print(groceries[0][2]) 
"""

groceries = [["apple", "orange", "banana", "coconut"],
            ["carrots", "celery", "potatoes"],
            ["milk", "cheese", "panner"]]

for colllection in groceries:
    for food in colllection:
        print(food, end=" ")
    print()