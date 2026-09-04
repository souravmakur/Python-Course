a = (1,2,3,4,5,6,7,45,8,"false", False, 1.34, 345)
# a[0] = 11      #TypeError: 'tuple' object does not support item assignment.
print(a)       #Tuples are immutable.

no = a.count(45) #it will tell me how many times 45 occurs in the tuple.
print(no)

idx = a.index(4) #it will give the index of the element 4.
print(idx)

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated = tuple1 + tuple2 #Concatenate 2 tuples
print(concatenated)

my_tuple = (1, 2, 3)
repeated = my_tuple * 3 #Repeat the tuple 3 times 
print(repeated) #Concatenate the same tuple thrice

print(2 in my_tuple) #Check if 2 is present in the tuple or not. It will return True or False
print(4 in my_tuple)
print(5 not in my_tuple) #Check if 5 is not present in the tuple or not. It will return True or False
print(3 not in my_tuple)

print(len(my_tuple)) #It will return the length of the tuple

sliced = my_tuple[1:3] #Slicing the tuple. It will return a new tuple with elements from index 1 to 2 (3 is excluded)
print(sliced) #remember that slicing a tuple will return a new tuple, it will not modify the original tuple.