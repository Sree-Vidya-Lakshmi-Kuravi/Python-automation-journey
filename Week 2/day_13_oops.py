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


# m1 = Manager("bvns", 140000, "Hi-Tech Enterprise")
# m1.display_info()    


## Bank Account

class BankAccount:
    
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def deposit(self, d_amt):
        if d_amt < 0:
            print("Deposited amount should not be negative.")
        else:
            self.__balance += d_amt
            print("Deposited Amount:", d_amt)
            print("Amount deposited successfully...")
            # print(f"Balance:", self.__balance)

    def withdraw(self, w_amt):
        if w_amt < 0:
            print("Withdrawal amount should not be negative")
        else:
            if w_amt > self.__balance:
                print("Insufficient Balance")
            else:
                self.__balance -= w_amt
                print("Withdrawal Amount:", w_amt)
                print("Amount withdrew successfully..")
                # print(f"Balance:", self.__balance)


    def check_balance(self):
        print("Account Holder Name:", self.name)
        print("Account Balance:", self.__balance)

b1 = BankAccount("BVNS", 150000)
# b1.check_balance()
b1.deposit(5000)
# b1.withdraw(9500)
b1.check_balance()
