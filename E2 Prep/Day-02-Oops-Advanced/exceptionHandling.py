# Exception handling prevents programs from crashing unexpectedly when errors occur.

try:
    a = int(input("Enter a number: "))
    print(10 / a)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Invalid input")

finally:
    print("Execution completed")
    
# --------------------------------------------------------------------
# KEYWORD             PURPOSE
# --------------------------------------------------------------------
# try        ---->    Executes code that might raise an exception.
# else       ---->    Handles an exception.
# except     ---->    Executes if no exception occurs.                
# finally    ---->    Executes whether an exception occurs or not.
# raise      ---->    Manually raises an exception.

class InvalidAgeError(Exception):
    pass

age = 15

if age < 18:
    raise InvalidAgeError("Age must be 18 or above")