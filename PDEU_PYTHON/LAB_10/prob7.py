import pickle

class Employee:
    def __init__(self, empcode, empname, doj, salary):
        self.empcode = empcode
        self.empname = empname
        self.doj = doj
        self.salary = salary

emp = Employee(101, 'Jeel', '2023-06-01', 70000)

# Serialization
with open('employee.pkl', 'wb') as f:
    pickle.dump(emp, f)

# Deserialization
with open('employee.pkl', 'rb') as f:
    loaded_emp = pickle.load(f)

print(vars(loaded_emp))
