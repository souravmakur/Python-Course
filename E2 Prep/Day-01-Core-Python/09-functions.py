# A function is a reusable block of code that can perform a particular task.

def greet():
    print("Hello, welcome to the world of Python!")
    
greet()

# Parameters and return values
def add(a, b):
    return a + b

result = add(10, 20)

print(result)

# Remember the distinction:
# - print() displays something.
# - return sends a value back to the caller.

# A. Positional Arguments
def introduce(name, age):
    print(name, age)
    
introduce("Sourav", 24)

#B. Keyword Arguments
introduce(age=25, name="Sourav")

#C. Default Arguments
def greeet(name="Guest"):
    print(f"Hello, {name}")

greeet()              #Hello, Guest
greeet("Sourav")      #Hello, Sourav

#D. *args
# Allows a function to receive a variable name of positional arguments.

def add_numbers(*args):
    print(args)        #(10, 20, 30, 40)
    return sum(args) 

print(add_numbers(10,20,30,40)) #100

#E. **kwargs
# Allows a function to receive a variable number of keyword arguments.

def display_details(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

display_details(
    name="Sourav",
    age=24,
    role="Developer"
)

# Inside the function, kwargs is a dictionary.

# Lambda Functions
# Lambda functions are small anonymous functions.

# Normal function:
def square(n):
    return n * n

# Lambda Function
square = lambda n: n * n
print(square(5))

add = lambda a, b: a + b
print(add(10, 20))

# Map
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda n: n ** 2, numbers))
print(squares)
