# 1. Write a python program to create a dictionary of hindi words and their english translation. Provide user with an option to look it up!

hindi_to_english = {
    "Namaste": "Hello",
    "Dhanyavad": "Thank you",
    "Kripiya": "Please",
    "Maaf Kijye": "Excuse me",
    "Haan": "Yes",
    "Nahi": "No"
}

def lookup_translation(word):
    return hindi_to_english.get(word, "Translation not found.") # it will either return the translation or "Translation not found." if the word is not in the dictionary.

def lookup_translation2(word):
    if word in hindi_to_english:
        return hindi_to_english[word]
    else:
        return "Translation not found."
    
word = input("Enter a Hindi word: ")
print(lookup_translation(word))
print(lookup_translation2(word))


# 2. Write a python program to take input from user and only show unique values.
set1 = set()
print("This is an empty set: ", set1)
for i in range(8):
    set1.add(input("enter a number: "))
    
print(set1)


# 3. Can we have a set with 18(int) and '18'(str) as elements? Write a python program to check this.
set2 = {18, '18'}
print("Set with 18 (int) and '18' (str): ", set2)

# 4. What wil be the length of the following set?
s = set()
s.add(20)
s.add(20.0) # This will not be added as a new element because 20 and 20.0 are considered equal in Python.
s.add('20')

print(s)

# 5. What is the type of s1
s1 = {}
print("Type of s1:", type(s1))  # It will print <class 'dict'> because {} creates an empty dictionary, not a set. To create an empty set, you should use set().

# 6. Create an empty dictionary. Allow 4 friends to enter their favorite 
#    language as value and use keys as their names. Assume that the names are unique.

dictionary = {}
for i in range(4):
    key = input("Enter your name: ")
    value = input("Enter your favorite programming language: ")
    dictionary[key] = value
    
print(dictionary)


# 7. If the names of two friends are the same, what will happen to the program 6
    # The last entered value for that key will overwrite the previous one.
    

# 8. If the favorite languages of two friends are the same, what will happen to the program 6
    # Nothing will happen. The dictionary will simply have the same value for both keys.
    

# 9. Can you change the values inside a list which is contained in Set s2

s2 = {8, 7, 12, "Harry", [1, 2, 3]}  
# This will raise a TypeError because lists are mutable and cannot be added to a set.
