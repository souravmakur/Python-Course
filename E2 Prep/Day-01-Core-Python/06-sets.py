# A set is an unordered collection of unique, hashable elements.

numbers = {10, 20, 30, 10, 20}
print(numbers)
# The order of elements is not guaranteed.

# Important set operations:-
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))

# Operation	                     Meaning.

# union()	                     All unique elements.
# intersection()	             Common elements.
# difference()	                 Elements in first set but not second.
# symmetric_difference()	     Elements in either set but not both.

numbers = {10, 20, 30}

numbers.add(40)
numbers.update([50, 60])
numbers.remove(20)
numbers.discard(100)

# Difference between remove() and discard():
# - remove() raises KeyError if the element doesn't exist.
# - discard() does not raise an error.
# An empty set is created using:

empty_set = set() 
#Not {}, because that creates an empty dictionary.