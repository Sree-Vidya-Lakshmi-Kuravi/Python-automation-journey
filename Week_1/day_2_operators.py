## Mini Project 01 - Calculator
print("1. Addition\n 2. Subtraction\n 3. Multiplication\n 4. Division")
choice = int(input("Enter the operation to be performed (1, 2, 3, 4)\n"))

num1 = int(input("Enter num1:"))
num2 = int(input("Enter num2:"))

if choice == 1:
    add = num1 + num2
    print(f"{num1} + {num2} = {add}")

elif choice == 2:
    subtract = num1 - num2
    print(f"{num1} - {num2} = {subtract}")

elif choice == 3:
    mul = num1 * num2
    print(f"{num1} * {num2} = {mul}")

elif choice == 4:
    div = num1 / num2
    print(f"{num1} / {num2} = {div}")

else:
    print("Select the correct operation to perform.")


## Number Guessing Game
import random
computer = random.randint(1, 10)
user = int(input("Guess the number:"))
while user:

    if user > computer:
        print("Your number is too high. Guess again.")

    elif user < computer:
        print("Your number is too low. Guess again.")

    else:
        print("Correct Guess. Congratulations !!!")

    break
