# C. Polymorphism
# Polymorphism means the same method name can behave differently depending on the object or class.

class Dog:
    def sound(self):
        print("Barks")

class Cat:
    def sound(self):
        print("Meows")

animals = [Dog(), Cat()]
for animal in animals:
    animal.sound()  # Output: Barks, Meows


# The same sound() method produces different results.
# Python also supports polymorphism through method overriding, 
# where a child class provides its own implementation of a parent method
