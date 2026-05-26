from day_15_string_utils import *

while True:
    print("--- STRING OPERATIONS ---")

    print("1. Reverse String\n2. Palindrome Check\n3. Vowel Count\n4. Exit")

    ch = int(input("Enter the choice: "))

    if ch == 4:
        break

    str = input("Enter the string:")

    if ch == 1:
        print("Reversing a string:")
        print(reverse_string(str))


    elif ch == 2:
        print("Palindrome Check:")
        print(palindrome_check(str))

    elif ch == 3:
        print("Number of vowels:")
        print(vowel_count(str))

    else:
        print("Wrong choice")