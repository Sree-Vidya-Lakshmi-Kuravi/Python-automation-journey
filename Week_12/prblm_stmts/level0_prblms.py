# ===== 1. Multi-Item Bill with Tiered Discount =====

def calculate_final_bill(item_prices: list, tax_rate: int):
    sub_total = 0
    for price in item_prices:
        sub_total += price

    # Conditional Discount
    if sub_total > 1000:
        discount_percent = 0.10
    elif 500 <= sub_total <= 1000:
        discount_percent = 0.05
    else:
        discount_percent = 0.0

    # Discount
    discount_subtotal = sub_total * (1 - discount_percent)
    tax_amount = discount_subtotal * (tax_rate / 100)
    total_tax_percent = discount_subtotal + tax_amount
    return round(total_tax_percent, 2)

# print(calculate_final_bill([23, 45, 89, 44, 55], 5))


# ===== 2. Vowel, Consonant, and Digit Tally =====
def analyze_text(sentence):
    seg_dict = {"vowels": 0, "consonants": 0, "digits": 0, "spaces": 0}
    vowels = "aeiou"

    for char in sentence.strip():
        low_char = char.lower()
        if low_char in vowels:
            seg_dict["vowels"] += 1
        elif low_char.isalpha() and low_char not in vowels:
            seg_dict["consonants"] += 1
        elif char.isdigit():
            seg_dict["digits"] += 1
        elif char == ' ':
            seg_dict["spaces"] += 1

    return seg_dict 

# print(analyze_text("Expecto Patronum from Harry Potter 7684054"))


# ===== 3. Prime Number Checker and Range Generator =====
def is_prime(n):
    if n == 0 or n == 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False

    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def get_primes_in_range(start, end):
    primes = []
    for p in range(start, end + 1):
        if is_prime(p):
            primes.append(p)

    return primes

prime_num1 = is_prime(2)
prime_num2 = is_prime(1)
prime_num3 = is_prime(4)
prime_num4 = is_prime(5)
range_num = get_primes_in_range(2, 5)
print(prime_num1, prime_num2, prime_num3, prime_num4)
print(range_num)