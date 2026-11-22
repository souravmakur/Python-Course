# Python can interact with databases to store, retrieve, update and delete data.
# For today's practice, we'll use SQLite, which comes built into Python.

import sqlite3

conn = sqlite3.connect("employees.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    salary INTEGER
)
""")

conn.commit()
conn.close()

#  This creates a database and an employees table.


# Insert data
import sqlite3

conn = sqlite3.connect("employees.db")
cursor = conn.cursor()

cursor.execute(
    "INSERT INTO employees (name, salary) VALUES (?, ?)",
    ("Sourav", 30000)
)

conn.commit()
conn.close()

# Use parameterised queries (?) instead of directly inserting user input into SQL 
# strings. This helps prevent SQL injection.


#Retreive data
import sqlite3

conn = sqlite3.connect("employees.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM employees")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()

# Update and delete

cursor.execute(
    "UPDATE employees SET salary = ? WHERE name = ?",
    (40000, "Sourav")
)

cursor.execute(
    "DELETE FROM employees WHERE name = ?",
    ("Sourav",)
)
