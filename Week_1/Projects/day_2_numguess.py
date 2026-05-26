import random

print("============ WELCOME TO NUMBER GUESSING GAME ============")

print("Guidelines:")
print("User guesses a number and that should match with the number guessed by the computer.")

c = random.randint(1, 15)
while True:
    u = int(input("Make a guess between 1 and 15: "))

    if u > c:
        print("Your guess is too high. Guess again.")

    elif u < c:
        print("Your guess is too low. Guess again.")

    elif u == c:
        print("Congratulations!!! You made a right guess.")
        break