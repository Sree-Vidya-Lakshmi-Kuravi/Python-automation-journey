## OOPS

# Employee System
class Employee:
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):

    def __init__(self, name, salary, dept):
        super().__init__(name, salary)
        self.dept = dept

    def display_info(self):
        print("Employee Name:", self.name)
        print("Employee Salary:", self.salary)
        print("Employee Department:", self.dept)
        

m1 = Manager("bvns", 140000, "Hi-Tech Enterprise")
m1.display_info()      
