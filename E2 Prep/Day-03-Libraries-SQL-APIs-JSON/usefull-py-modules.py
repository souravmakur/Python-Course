# A. datetime
# Used for handling dates and time.

from datetime import datetime
now = datetime.now()

print(now)
print(now.strftime("%d-%m-%Y"))

# METHOD	               PUROPOSE
# datetime.now()	       Current date and time
# strftime()	           Format date and time
# strptime()	           Convert string to datetime

# B. Collections - Provides specialised data structures.
from collections import Counter
items = ["apple", "banana", "apple", "orange", "banana", "apple"]

print(Counter(items))

# C. re- Regular expressions
# used for pattern matching in strings 

import re
text = "My employee ID is 12345"
result = re.findall(r"\d+", text)

print(result) #['12345']


# METHOD                       PURPOSE
# re.search()	    ->         Finds the first match
# re.findall()	    ->         Returns all matches
# re.sub()	        ->         Replaces matching text
# re.match()	    ->         Checks for a match at the beginning














