while True:
    print("================== WELCOME ==================")
    print("""1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exit""")

    op = int(input("Select the operation to perform:"))

    if op == 5:
        print("Closing the calculator..")
        print("Calculator Closed")
        break

    num1 = float(input("num1: "))
    num2 = float(input("num2: "))

    def add(num1, num2): return num1 + num2
    def subtract(num1, num2): return abs(num1 - num2)
    def multiply(num1, num2): return num1 * num2
    def divide(num1, num2): return num1 / num2


    if op == 1:
        print("Addition result:")
        print(add(num1, num2))

    elif op == 2:
        print("Subtraction result:")
        print(subtract(num1, num2))

    elif op == 3:
        print("Multiplication result:")
        print(multiply(num1, num2))

    elif op == 4:
        print("Division result:")
        if num2 != 0:
            print(divide(num1, num2))
        else:
            print("Cannot divide by zero.")

    else:
        print("Enter the correct operation to be performed. Try again.")




