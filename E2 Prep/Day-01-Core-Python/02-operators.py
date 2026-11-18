# Operators perform operations on variables and values. In Python, we have the following types of operators:

# A. Arithmetic Operators: Used to perform mathematical operations like addition, subtraction, multiplication, division, etc.

a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333...
print(a // b)  # 3
print(a % b)   # 1
print(a ** b)  # 1000

# / always performs division and returns a float.
# // performs floor division.
# % returns the remainder.
# ** performs exponentiation.

# B. Comparison Operators: Used to compare two values and return a boolean result (True or False).

c = 10
d = 20

print(c == d)  # False
print(c != d)  # True
print(c > d)   # False
print(c < d)   # True
print(c >= d)  # False
print(c <= d)  # True

# C. Logical Operators: Used to combine conditional statements.

age = 24
has_id = True

print(age >= 18 and has_id)  # True
print(age < 18 or has_id)    # True
print(not has_id)            # False

# Python uses and, or, and not, unlike Java's &&, ||, and !.

# D. Assignment Operators: Used to assign values to variables.

x = 10
x += 5
x -= 2
x *= 2
x /= 2
x //= 2
x %= 3

# E. Membership Operators: Used to test if a sequence contains a certain value.
numbers = [10, 20, 30, 40]

print(20 in numbers)      # True
print(50 not in numbers)  # True

# F. Identity Operators: Used to compare the memory locations of two objects.
# "is" and "is not" check whether two references point to the same object.

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a == c)  # True
print(a is c)  # False
print(a is b)  # True

# Very important for E2: "==" compares values; "is" compares object identity.