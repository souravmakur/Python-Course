# A list is an ordered, mutable collection that allows duplicate elements.

numbers = [10, 20, 30, 40, 20]

print(numbers[0])
print(numbers[-1])
print(numbers[1:4])

# Important list methods

numbers = [10, 20, 30]

numbers.append(40)       # Adds one element
numbers.insert(1, 15)    # Inserts at index
numbers.extend([50, 60]) # Adds multiple elements

numbers.remove(20)       # Removes first matching value
numbers.pop()            # Removes last element
numbers.pop(0)           # Removes element at index 0

numbers.sort()           # Sorts original list
numbers.reverse()        # Reverses original list

print(numbers)

# methods :-

# append()	Adds one element
# extend()	Adds elements from an iterable
# insert()	Adds at a specific index
# remove()	Removes by value
# pop()	    Removes and returns by index
# clear()	Removes all elements
# index()	Returns first matching index
# count()	Counts occurrences
# sort()	Sorts the original list
# sorted()	Returns a new sorted list

# List Comprehension: A concise way to create lists.

# instead of :-
numbers = [1, 2, 3, 4, 5]

squares = []

for n in numbers:
    squares.append(n ** 2)

print(squares)

# You can write:
numbers = [1, 2, 3, 4, 5]
squares = [n ** 2 for n in numbers]

print(squares)

# With conditions:
even_numbers = [n for n in numbers if n % 2 == 0]

print(even_numbers)


# Nested Lists

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0][1])  # 2
print(matrix[2][2])  # 9

# List aliasing

a = [1, 2, 3]
b = a

b.append(4)
print(a)