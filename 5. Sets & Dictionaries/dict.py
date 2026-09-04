# It is unordered that means the order of the elements is not fixed. It can change every time you run the program.
# It is mutable that means we can change the values of the dictionary.
# It is indexed that means we can access the values of the dictionary using the keys.
# It cannot contain duplicate keys that means we cannot have two keys with the same name in a dictionary.

# This here is a dictionary with keys as names and values as marks of students.
marks = {
    "Harry" : 100,  #List of key value pairs
    "Rohan" : 90,
    "Ram" : 80
}

print(marks["Harry"]) # prints 100
print(marks , type(marks)) # prints the dictionary and its type

# Here are some methods that can be used with dictionaries.

print(marks.keys()) # returns a list of all the keys in the dictionary

print(marks.values()) # returns a list of all the values in the dictionary

print(marks.items()) # returns a list of all the key-value pairs in the dictionary

print(marks.get("Harry")) # returns the value of the key "Harry"

marks.update({"Harry" : 95}) # updates the value of the key "Harry" to 95

print(marks) # prints the updated dictionary

print(marks.clear()) # clears the dictionary

print(marks.pop("Rohan")) # removes the key "Rohan" and its value from the dictionary

