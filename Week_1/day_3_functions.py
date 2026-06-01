## Function to find square
def find_square(n):
    return n ** 2


## Function to check prime
def check_prime(n):
    if n == 0 or n == 1:
        print("Neither Prime nor Composite")
    
    for i in range(2, n):
        if n % i != 0:
            return "Not Prime"
        else:
            return "Prime"
    else:
        return "Prime"

print(check_prime(2))
print(check_prime(23))



## Function to reverse a string
def rev_string(s):
    return s[::-1]


## Function to count vowels
def count_vowels(s):
    count = 0
    if s in 'aeiou' or s in 'AEIOU':
        count += 1
        return count


## Function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    fact = 1
    while n and n != 1:
        fact *= n  # fact = fact * n
        n -= 1  # n = n - 1
        print(n)
    return fact


## Function to check palindrome
def is_palindrome(n):
    u = 0
    p = 0
    n1 = n

    while n:
        u = n % 10
        p = p * 10 + u
        n = n // 10
        print(u, p, n)
    
    return p == n1

print(is_palindrome(12321))
print(is_palindrome(1465))
