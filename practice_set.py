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


# 3. Check that tuple type cannot be changed in python.
t = (1, 2, 3)
# t[0] = 5  # This will raise an error
print(t)

#4 Write a program to sum all the items in a list.
list1 = [1, 2, 3]
sum = 0
for i in range(len(list1)):
    sum = sum + list1[i]
    
print(sum)
