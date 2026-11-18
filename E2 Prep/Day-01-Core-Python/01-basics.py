# Unlike Java, Python is dynamically typed. You don't need to declare the data type explicitly.

# In Java:
# int age = 24;
# String name = "Sourav";
# double salary = 23000.50;

age = 24
name = "Sourav"
salary = 23000.50

# Python automatically determines the type based on the assigned value.

age = 24  # Integer
name = "Sourav"  # String
salary = 23000.50  # Float
list = [1, 2, 3, 4, 5]  # List
tuple = (1, 2, 3, 4, 5)  # Tuple
set = {1, 2, 3, 4, 5}  # Set
dict = {"name": "Sourav", "age": 24, "salary": 23000.50}  # Dictionary

# to check the type of a variable, you can use the built-in `type()` function.
print(type(age))  # <class 'int'>
print(type(name))  # <class 'str'>
print(type(salary))  # <class 'float'>
print(type(list))  # <class 'list'>
print(type(tuple))  # <class 'tuple'>
print(type(set))  # <class 'set'>
print(type(dict))  # <class 'dict'>

# Type conversion (casting) can be done using built-in functions like `int()`, `float()`, `str()`, etc.
# You can convert one data type into another.

age = "24"
print(type(age))
age = int(age)
print(age)
print(type(age))

#Other examples of type conversion:
 
x = int("100")
y = float("10.5")
z = str(500)
a = list((1, 2, 3))
b = tuple([1, 2, 3])

# Remember: int("hello") throws a ValueError.

# Important concept: Muttable vs Immutable
    # Mutable : Objects whose contents can be changed after creation.
    # Immutable : Objects whose contents cannot be changed after creation.

# Mutable:	      Immutable:
    
# List	          Integer
# Dictionary	  Float
# Set	          String
# 	              Tuple (its structure)
# 	              Boolean

# One important nuance: a tuple cannot have its elements reassigned, 
# but it can contain a mutable object such as a list, and that list can still be modified.

# Interview question: Is Python pass-by-value or pass-by-reference?

# Python uses object-reference passing (often described as call by sharing). 
# Function parameters receive references to objects, not independent copies.

def change(x):
    x.append(4)  # Modifies the original list
    
numbers = [1, 2, 3]
change(numbers)
print(numbers)  # Output: [1, 2, 3, 4] - The original list is modified

# but what if

def change(x):
    x = [4, 5, 6]  # Reassigns x to a new list, does not modify the original list

numberss = [1, 2, 3]

change(numberss)
print(numberss)  # Output: [1, 2, 3] - The original list remains unchanged

# "Python uses object-reference passing, also known as call by sharing. 
# Function parameters receive references to the same objects rather than independent copies. 
# Therefore, modifying a mutable object inside a function affects the original object, but reassigning 
# the parameter does not affect the original variable."
