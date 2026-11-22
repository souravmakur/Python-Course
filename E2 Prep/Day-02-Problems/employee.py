class Employee:
  def __init__(self, name, emp_id, salary):
    self.name = name
    self.emp_id = emp_id
    self.salary = salary

  def displayInfo(self):
    return f"Name: {self.name} | Employee Id: {self.emp_id} | Salary: {self.salary}"

class Developer(Employee):
  def __init__(self, name, emp_id, salary, programming_language):
    super().__init__(name, emp_id, salary)
    self.programming_language = programming_language

  def displayInfo(self):
    return f"{super().displayInfo()} | Programming Language: {self.programming_language}"

class Manager(Employee):
  def __init__(self, name, emp_id, salary, team_size):
    super().__init__(name , emp_id, salary)
    self.team_size = team_size

  def displayInfo(self):
    return f"{super().displayInfo()} | Team Size: {self.team_size}"

if __name__ == "__main__":
  dev = Developer("Sourav", 101, 85000, "Python")
  mgr = Manager("Rajeev", 102, 120000, 12)
  emp = Employee("Vivek", 103, 130000)

print(dev.displayInfo())
print(mgr.displayInfo())
print(emp.displayInfo())


  