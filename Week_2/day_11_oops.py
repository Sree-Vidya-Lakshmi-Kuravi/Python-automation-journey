## OOPS Concepts

# Student Class
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name: ", self.name)
        print("Marks: ", self.marks)

s1 = Student('YB', 99)
s1.display()


# Employee Class
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def yearly_salary(self):
        print("Monthly salary:\n", self.salary)
        print("Yearly salary: ")
        return 12 * self.salary

e1 = Employee('bvns', 7000)
print(e1.yearly_salary())


## Recctangle Class
class Rectangle:
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        print("Area of rectangle: ")
        return self.l * self.b

    def perimeter(self):
        print("Perimeter of rectangle: ")
        return 2 * (self.l + self.b)

r1 = Rectangle(12, 5)
print(r1.area())
print(r1.perimeter())


## Circle class
class Circle:
    def __init__(self, r):
        self. r = r

    def area(self):
        return 3.14 * self.r * self.r

    def circumference(self):
        return 2 * 3.14 * self.r

c1 = Circle(4)
print(f"Area of circle is: ", c1.area())
print(f"Circumference of circle is: ", c1.circumference())


## Bank Account Class
class BankAccount:
    def __init__(self, acc_h, bal):
        self.acc_h = acc_h
        self.bal = bal

    def deposit(self, d_amt):
        self.bal += d_amt
        print(f"Your amount {d_amt} has been deposited successfully")
        print("Your total balance is: ", self.bal)

    def withdraw(self, w_amt):
        if self.bal < w_amt:
            print("Insufficient balance. You cannot withdraw the amount")
        else:
            self.bal -= w_amt
            print(f"Your amount {w_amt} has been withdrew successfully")
        print("Your total balance is: ", self.bal)

    def check_balance(self):
        print("Account Holder Name: ", self.acc_h)
        print("Balance Amount: ", float(self.bal))

b1 = BankAccount("BVNS", 37500)
b1.deposit(100)
b1.withdraw(500)
b1.check_balance()