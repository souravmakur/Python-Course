# A. List Comprehension -> A concise way to create lists.

numbers = [1, 2, 3, 4, 5]

squares = [x * x for x in numbers]
even = [x for x in numbers if x % 2 == 0]

print(squares)
print(even) 

# B. Generators
# Generators produce values one at a time using yield, 
# rather than storing the entire sequence in memory.

def numbers():
    for i in range(1,4):
        j = i ** i 
        yield j
    
for n in numbers():
    print(n)
    

# C. Iterators
# An iteretor is an object that returns 
# values one at a time using next()
nums = [10, 20, 30]
it = iter(nums)

print(next(it))
print(next(it))
print(next(it))


# D. Decorators
# A decorator modifies or extends the behaviour of a function wthout
# modifying the original function's code directly.

def decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@decorator
def greet():
    print("Hello")
    
greet()

# E. File Handling
with open("data.txt", "w") as file:
    file.write("Python E2 Preparation")
    
with open("data.txt", "r") as file:
    print(file.read())
    

# MODE               MEANING
# r                  Read               
# w                  Write, overwrites existing content   
# a                  Append   
# x                  Create new file   

# with automatically manages file closure.