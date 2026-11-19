# A tuple is an ordered, immutable collection.

coordinates = (10, 20, 30)

print(coordinates[0])
print(coordinates[-1])

# Unlike lists, you cannot change tuple elements after creation.

numbers = (10, 20, 30, 10)

print(numbers.count(10))
print(numbers.index(20))

# Packing and unpacking
person = ("Sourav", 24, "Developer")

name, age, profession = person

print(name)
print(age)
print(profession)

# Single-element tuple
a = (10)
b = (10,)

print(type(a))  # int
print(type(b))  # tuple

# The comma makes it a tuple, not the parentheses alone.

# When to use a tuple?
# Use a tuple when you want a fixed collection of values 
# that should not be reassigned, such as coordinates, 
# configuration values or records.