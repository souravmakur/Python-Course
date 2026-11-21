# Constructor and super()

# super() allows a child class to call methods, 
# particularly the constructor, of its parent class.

class Employee:
    def __init__(self, name):
        self.name = name
    
class Developer(Employee):
    def __init__(self, name, language):
        super().__init__(name)
        self.language = language

d = Developer("Sourav", "Python")
print(d.name , d.language) # Output: Sourav Python


class Employee:
    def __init__(self, name):
        self.name = name
    
    def show(self):
        print(self.name)
        
    @classmethod
    def class_method(cls):
        print(cls.company)
        
    @staticmethod
    def greet():
        print("Welcome")