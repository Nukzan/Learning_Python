class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

emp1 = Employee("Zara", 2000)
print("Name : ", emp1.name, ",","Salary : ", emp1.salary)
emp2 = Employee("Manni", 5000)
print("Name : ", emp2.name, ",","Salary : ", emp2.salary)

class Employee2:
        def __init__(self, name, dailywage, weekly):
            self.name = name
            self.salary = dailywage * weekly

emp3 = Employee2("Zara", 200, 5)
print("Name : ", emp3.name, ",","Salary : ", emp3.salary)