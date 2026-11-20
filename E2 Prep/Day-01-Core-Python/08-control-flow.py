# Control flow determines which statements execute and how many times.

# A. if, elif and else
marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Fail")
    
# Python uses indentation to define code blocks instead of curly braces.

# B. for loop
for i in range(1, 6):
    print(i)
    
# range(start, stop, step):
range(1, 10, 2) #Produces 1, 3, 5, 7, 9.

#C. while loop
count = 1

while count <= 5:
    print(count)
    count += 1
    
# D. break, continue and pass

for i in range(1, 6):

    if i == 3:
        continue

    if i == 5:
        break

    print(i)
    
# break: Terminates the loop.
# continue: Skips the current iteration.
# pass: Does nothing; acts as a placeholder.

#E. enumerate()
# Useful when you need both the index and value.
names = ["Amit", "Rahul", "Sourav"]

for index, name in enumerate(names):
    print(index, name)
    
# F. zip()
# Iterates over multiple iterables together.
names = ["Amit", "Rahul", "Sourav"]
ages = [23, 25, 24]

for name, age in zip(names, ages):
    print(name, age)
    
# G. Loop's else clause
# A Python-specific feature worth knowing.
for i in range(5):
    print(i)
else:
    print("Loop completed")
    
# The else executes when the loop finishes normally, without being terminated by break.

