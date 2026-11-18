# "Strings are immutable sequences of Unicode characters."
name = "Sourav Makur"

print(name[0])    # S
print(name[-1])   # r
print(name[0:6])  # Sourav
print(name[7:]) # Makur

# String slicing:
# syntax: string[start:stop:step]

text = "PYTHON"

print(text[0:3])   # PYT
print(text[:4])    # PYTH
print(text[2:])    # THON
print(text[::-1])  # NOHTYP
print(text[::2])   # PTO


name2 = "Sourav Makur"
print(name2[::-1])


# Important String Methods:

text = "  hello python  "

print(text.upper())
print(text.lower())
print(text.title()) # Hello Python
print(text.strip()) # removes leading and trailing whitespace
print(text.replace("python", "java"))
print(text.split()) # splits the string into a list of substrings
print(text.find("python")) # finds the index of the first occurrence of "python"
print(text.count("o")) # counts the number of occurrences of "o"
print(text.startswith("  hello")) # checks if the string starts with "  hello"
print(text.endswith("  ")) # checks if the string ends with "  "

# String formatting:
name = "Sourav"
age = 24

print(f"My name is {name} and I am {age} years old.")

# You can also format numbers:
price = 99.5678

print(f"Price: {price:.2f}") #Output: Price: 99.57

# String immutability
name = "Python"

# name[0] = "J"  # TypeError

name = "J" + name[1:]

print(name)  # Jython