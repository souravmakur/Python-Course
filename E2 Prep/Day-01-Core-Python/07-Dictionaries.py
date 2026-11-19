# A dictionary stores key-value pairs.
employee = {
    "name": "Sourav",
    "age": 24,
    "department": "Engineering",
    "salary": 23000
}

print(employee["name"])
print(employee.get("salary"))

# Difference:
# - employee["city"] raises KeyError if the key doesn't exist.
# - employee.get("city") returns None by default.

# Important dictionary methods
employee.keys()
employee.values()
employee.items()
employee.update({"age": 25})
employee.pop("salary")
employee.setdefault("city", "Kolkata")

# Iterating through a dictionary

employee = {
    "name": "Sourav",
    "age": 24,
    "salary": 23000
}

for key, value in employee.items():
    print(key, value)
    
# Dictionary comprehension

numbers = [1, 2, 3, 4, 5]
squares = {n: n ** 2 for n in numbers}
print(squares)

# Frequency counting

text = "banana"

frequency = {}

for char in text:
    frequency[char] = frequency.get(char, 0) + 1

print(frequency)
