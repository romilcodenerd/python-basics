# What is dictionary?

# A dictionary is a collection of key value pairs.
# Each item has a key and value:

# Dictionary methods:

#keys()-returns all keys
#value()-returns all values
#items()-returns key-value pairs
#get(key)-returns value of key (safe way)
#pop (key)-removes and returns value of key
#clear()-removes all key value pairs
#update(dict2)-updates with another dictionary's
#values.

# program:

student={
    "name":"romil",
    "age":26,
    "course":"python"
}

student["city"]="amreli"
student ["age"]=26
student.update({"age":23})
print(student)
del student ["age"]


#Looping through dictionary
car={
    "brand":"Toyota",
    "model":"fortuner",
    "year":"2022"
}

car["year"]
car["brand"]
car["model"]
print(car)
print(car.keys())
print(car.values())
print(car.items())
print(car.get("brand"))
print(car.pop("brand"))
print(car.clear())
car = {"brand": "Ford"}
dict2 = {"brand": "BMW"}
car.update(dict2)
print(car["brand"])


# Using keys() Method:
# This method uses the keys() function to get a view object 
# of the dictionary’s keys and then converts it into a list.

r = {'name':'romil', 'age':26, 'city':'Tokyo'}
a = list(r.keys())
print(a) 
