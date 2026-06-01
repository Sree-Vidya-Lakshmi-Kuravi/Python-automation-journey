## add two numbers
num1 = int(input("Enter num1:"))
num2 = int(input("Enter num2:"))
def sum_of_two_num(num1, num2):
    return num1 + num2

print(sum_of_two_num(num1, num2))


## Check Even or Odd
num = int(input("Enter the number:"))
def even_or_odd(num):
    if num % 2 == 0:
        print(f"{num} is Even")
    print(f"{num} is Odd")


## Largest of 3 numbers
num1 = int(input("Enter num1:"))
num2 = int(input("Enter num2:"))
num3 = int(input("Enter num3:"))

def largest_of_three(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        print(f"{num1} is greater than {num2} and {num3}")

    elif num2 > num3 and num2 > num1:
        print(f"{num2} is greater than {num1} and {num3}")

    else:
        print(f"{num3} is greater than {num1} and {num2}")


## Multiplication Table
table = int(input("Enter the number to generate the table for:"))

def mul_table(table):
    for i in range(1, 11):
        mul = table * i
        print(f"{table} x {i} = {mul}")


## Sum of first N numbers
N = int(input("Enter the value of N:"))

def sum_of_N_num(N):
    total_sum = 0
    for i in range(0, N+1):
        total_sum += i
    print(f"The sum is: {total_sum}")


## Reverse a String
string = input("Enter the string:")

def rev_string(string):
    return string[::-1]


## Count vowels in a string
string = input("Enter the string:")

def count_vowels(string):
    count = 0
    for s in string:
        if s in 'AEIOU' or s in 'aeiou':
            count += 1
    return count


## Fibonacci Series
num_range = int(input("Enter the number range:"))

def fibo(num_range):
    a = 0
    b = 1
    for i in range(num_range + 1):
        print(a, end = " ")
        next_num = a + b
        a = b
        b = next_num


## Prime Number Check
num = int(input("Enter the number:"))

def prime(num):
    if num == 0 or num == 1:
        print(f"{num} is neither Prime nor Composite.")
    elif num > 1:
        for i in range(2, n//2):  # 2, 3  n//2 = 4
            if (n % i == 0):
                print("Not prime")
                break
        else:
            print("Prime")
            

## Palindrome Check
num = int(input("Enter the number:"))

def palindrome(num):
    n1 = num
    p = 0
    while num:
        u = num % 10
        p = p * 10 + u
        num = num // 10
        print(u, p)

    if n1 == p:
        print("Palindrome")
    else:
        print("Not a Palindrome")

print(palindrome(num))



