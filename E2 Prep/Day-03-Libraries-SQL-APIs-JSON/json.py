# JSON in Python
# JSON is a commonly used format for exchangimg data between applications,
# expecially API and web applications

import json

student = {
    "name": "Sourav",
    "age": 24,
    "skills": ["Python", "Java"]
}

json_data = json.dumps(student)
print(json_data)

# json.dumps() converts Python objects into a JSON string.

import json
data = '{"name": "Sourav", "age": 24}'
student = json.loads(data)
print(student["name"])  #Sourav

# METHOD	              PURPOSE
# json.dumps()	          Python object → JSON string
# json.loads()	          JSON string → Python object
# json.dump()	          Writes JSON into a file
# json.load()	          Reads JSON from a file



# an excercise where i am converting a dict to a json & vice versa
employee = {
    "name" : "Sourav",
    "emp_id" : 2866503,
    "salary" : 23000
}

employee_json = json.dumps(employee)
print(employee_json)
employee_object = json.loads(employee_json)
print(employee_object)
print(employee["name"],',', employee["emp_id"],',', employee["salary"])

# OUTPUT
# {"name": "Sourav", "emp_id": 2866503, "salary": 23000}
# {'name': 'Sourav', 'emp_id': 2866503, 'salary': 23000}
# Sourav , 2866503 , 23000