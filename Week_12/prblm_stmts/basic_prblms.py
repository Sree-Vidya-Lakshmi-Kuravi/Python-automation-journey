## Basic Functions Implementation

def check_number(n):
    if n == 0:
        return "Zero"
    elif n < 0:
        return "Negative"
    else:
        return "Positive"
# print(check_number(2))
# print(check_number(0))
# print(check_number(-2))

def check_even_odd(n):
    if n == 1:
        return "Neither Odd Nor Even"
    elif n % 2 == 0:
        return "Even"
    else:
        return "Odd"
# print(check_even_odd(1))
# print(check_even_odd(2))
# print(check_even_odd(43))

def largest_of_two_num(n1, n2):
    if n1 > n2:
        return "n1 is greater than n2"
    elif n1 < n2:
        return "n2 is greater than n1"
    else:
        return "n1 and n2 are equal"
# print(largest_of_two_num(2, 5))
# print(largest_of_two_num(4, 1))
# print(largest_of_two_num(4, 4))

def largest_of_three_num(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return "n1 is greater"
    elif n2 > n1 and n2 > n3:
        return "n2 is greater"
    elif n3 > n1 and n3 > n2:
        return "n3 is greater"
    else:
        return "all are equal"
# print(largest_of_three_num(0, 2, 3))
# print(largest_of_three_num(3, 2, 1))

def div_with_5(n):
    if n % 5 == 0:
        return f"{n} is divisible by 5"
    else:
        return f"{n} is not divisible by 5"
# print(div_with_5(3))
# print(div_with_5(0))
# print(div_with_5(5))

def age_cat(age):
    if age < 13:
        print("Child")
    elif 13 <= age <= 19:
        print("Teenager")
    elif 20 <= age <= 59:
        print("Adult")
    else:
        print("Senior")
# print(age_cat(3))
# print(age_cat(13))
# print(age_cat(23))
# print(age_cat(63))