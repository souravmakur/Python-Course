# A class is a blueprint, while an object is an instance of that blueprint.
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)
    
s1 = Student("Sourav", 24)
s1.display()

# class Student:       Defines a class.
#      __init__:       Constructor, called when an object is created.
#          self:       Refers to the current object.
#            s1:       An object of the Student class.