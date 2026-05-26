### EXCEPTION HANDLING

## Invalid integer input
def val_err():
    try:
        a = int(input("Enter the number: "))
        print("The given input is:", a)
    except ValueError:
        print(f"The input must be in integer. Please enter an integer value.")

# val_err()


## Divide by Zero
def zero_div_err():
    try:
        a = int(input("Enter a value: "))
        b = int(input(f"Enter the value with which {a} has to be divided with: "))
        d = a / b
        print(f"The division of {a} and {b} is: ", d)

    except ZeroDivisionError:
        print("The value of b must not be zero")
    
    except ValueError:
        print("The inputs must be in integers only")

# zero_div_err()


## File Not Found
path = 'Week2\\sample.txt'
def file_not_found_err():
    try:
        with open(path) as f:
            print(f)
    except FileNotFoundError:
        print("File not found. Please enter the correct file path") 

# file_not_found_err()


# ## Safe calculator
# def calculator():
#     print("----------- CALCULATOR -----------")
#     print("\n1. Add\n2. Divide")

#     ch = int(input("Enter the choice: "))
    
#     if ch == 1:
#         try:
#             a = int(input("Enter the value of a: "))
#             b = int(input("Enter the value of b: "))
#             s = a + b
#             print(f"The sum of {a} and {b} is: ", s)

#         except ValueError:
#             print("The inputs should be in integer only")

#     elif ch == 2:
#         try:
#             a = int(input("Enter the value of a: "))
#             b = int(input("Enter the value of b: "))
#             d = a / b
#             print(f"The division of {a} and {b} is: ", d)

#         except ZeroDivisionError:
#             print("The value of b should not be zero.")
        
#         except ValueError:
#             print("The inputs should be in integer only")


#     else:
#         try:
#             print("Wrong Choice")
#         except ValueError:
#             print("The input should only be in integers")

# calculator()

def calculator():

    try:
        while True:
            print("1. Add\n2. Divide\n3. Exit")
            ch = int(input("Enter your choice (1/2/3): "))

            if ch == 3:
                break

            elif ch == 1:
                a = int(input("Enter the value of a: "))
                b = int(input("Enter the value of b: "))
                s = a + b
                print(f"The sum of {a} and {b} is: ", s)

            elif ch == 2:
                a = int(input("Enter the value of a: "))
                b = int(input("Enter the value of b: "))
                d = a / b
                print(f"The division of {a} and {b} is: ", d)

            else:
                print("Select between 1, 2 and 3 choices")

            break
    
    except ValueError:
        print("The inputs must be in integers only.")
    
    except ZeroDivisionError:
        print("The value of b must not be zero")

    finally:
        print("Calculator closed")

# calculator()


