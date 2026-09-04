# A set in python is a collection of unique elements. 
# It is unordered and mutable, meaning you can add or remove elements from it. 
# Sets are defined using curly braces {} or the set() constructor.

# Creating a set
my_set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}

#Even if we add an element that already exists in the set, it will not be added again.
my_set = {1,2,2,2,3,4,5,6}
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

print(type(my_set))  # Output: <class 'set'>

# Here are a few common operations you can perform on sets:
# Adding elements
my_set.add(7)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6, 7}

# Removing elements
my_set.remove(3)
print(my_set)  # Output: {1, 2, 4, 5, 6, 7}

# Checking membership
print(4 in my_set)  # Output: True
print(3 in my_set)  # Output: False

# Set operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print(set_a.union(set_b))  # Output: {1, 2, 3, 4, 5, 6}

# Intersection
print(set_a.intersection(set_b))  # Output: {3, 4}