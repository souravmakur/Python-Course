# An API allows two applications to communicate and exchange data. 
# In Python, we commonly use APIs to retrieve or send data to external services.

# HTTP methods 

# METHOD	     PURPOSE
# GET	    ->     Retrieve data
# POST	    ->     Send or create data
# PUT	    ->     Update data
# PATCH	    ->     Partially update data
# DELETE	->     Delete data


# HTTP status codes

# Code	  ->      Meaning
# 200	  ->      OK
# 201	  ->      Created
# 400	  ->      Bad Request
# 401	  ->      Unauthorized
# 403	  ->      Forbidden
# 404	  ->      Not Found
# 500	  ->      Internal Server Error

# Using the requests library
# pip install requests

import requests
response = requests.get("https://jsonplaceholder.typicode.com/users")

print(response.status_code)
print(response.json())

# requests.get() sends a GET request.
# response.status_code returns the HTTP status code.
# response.json() converts the JSON response into Python data.

import requests
response = requests.get("https://jsonplaceholder.typicode.com/users")

if response.status_code == 200:
    users = response.json()

    for user in users:
        print(user["name"], user["email"])
else:
    print("Request failed")
    
    
    
# Handling API exceptions
import requests

try:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users",
        timeout=5
    )
    response.raise_for_status()
    print(response.json())

except requests.exceptions.RequestException as e:
    print("Error:", e)