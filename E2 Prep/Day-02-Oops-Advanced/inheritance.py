# B. Inheritance
# Inheritance allows a class to inherit attributes and methods from another class, promoting code reusability.
class Animal:
    def sound(self):
        print("Animal makes a sound")
        
class Dog(Animal):
    def bark(self):
        print("Dog barks")
        
d = Dog()
d.sound()  # Output: Animal makes a sound
d.bark()   # Output: Dog barks

# Type of Inheritance:
# 1. Single Inheritance - One child inherits from one parent.
 
#  -----------------------------------
#                                   
#               Parent Class
#                (Person)  
#   
#  -----------------------------------
#                   |
#                   |
#                   |
#                   |
#  -----------------------------------
#                                   
#               Child Class
#                (Student)  
#   
#  -----------------------------------

# 2. Multiple Inheritance - One child inherits from multiple parents.
# One child inherits from multiple parents.

# 3. Multilevel Inheritance 
# A child inherits from a parent, and then another child inherits from that child.

# 4. Hierarchical Inheritance - 
# Multiple children inherit from a single parent.
