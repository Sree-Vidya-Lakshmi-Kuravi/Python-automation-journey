## Math Functions

def factorial(n):
    if n == 0 or n == 1:
        return 1
    fact = 1
    while n and n != 1:
        fact *= n  # fact = fact * n
        n -= 1  # n = n - 1
        print(n)
    return fact


def prime_check(n):
    if n == 0 or n == 1:
        print("Neither Prime nor Composite")
    
    for i in range(2, n):
        if n % i != 0:
            return "Not Prime"
        else:
            return "Prime"
    else:
        return "Prime"


def fibonacci(num_range):
    a = 0
    b = 1
    for i in range(num_range + 1):
        print(a, end = " ")
        next_num = a + b
        a = b
        b = next_num
