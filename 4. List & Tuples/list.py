friends = ["Apple" , "Orange", 5, 4.45, "Aakash"]
print(friends[3])
friends[3] = 4
print(friends[3]) #Lists are muttable, it can be changed 

string = "Hello"
print(string)
# string[0] = "l"  #This will give me: TypeError: 'str' object does not support item assignment
                 #This happens because strings are immutable, they cannot be changed
                 
print(friends[1:4])

l1 =[6,8,3535,7,45,2124,2.1]
print(l1)

l1.append(91) #appends at the end of the list
print(l1)

l1.insert(3,123) #inserts at a particular position (index , value)
print(l1)

l1.sort() #sorts the list in ascending order
print(l1)

l1.reverse() #reverses the list
print(l1)

l1.pop(3) #removes third index
print(l1)
