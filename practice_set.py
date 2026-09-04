# 1. Write a program to store 7 fruits in a list entered by the user.
fruits = []
for i in range(7):
    fruit = input("Enter the name of fruit: ")
    fruits.append(fruit)
    print(fruits)
    
# 2. Write a program to store marks of 6 students in a list entered by the user.  
marks = []
number = 1
for i in range(6):
    mark = input("Enter the marks of student " + str(number) + ":" )
    marks.append(mark)
    number += 1
    
print(marks)
  
