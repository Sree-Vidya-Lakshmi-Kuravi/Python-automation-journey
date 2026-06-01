## Password Strength Checker

# Program should check:
# uppercase letter
# lowercase letter
# number
# special character
# minimum length

import string 
password = '22HM1A0569#siri'

upp = string.ascii_uppercase
low = string.ascii_lowercase
spl = string.punctuation
num = string.digits

min_len = True if len(password) >= 8 else False
upp_l = any(p in password for p in upp)
low_l = any(p in password for p in low)
spl_c = any(p in password for p in spl)
num_c = any(p in password for p in num)

if min_len and upp_l and low_l and spl_c and num_c:
    print("Strong Password")
else:
    print("Weak password")


pw = '22HM1A0569#siri'

def min_length(pw):
    if len(pw) < 8:
        print("The password must contain ")
