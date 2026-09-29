# === 1. Shopping Bill Calculator ===
def bill_calc(prices: list):
    total_amt = 0
    for p in prices:
        total_amt += p
    print("Total Amount: ", total_amt)

    if total_amt > 2000:
        discount = total_amt * 0.10
    elif 1000 <= total_amt <= 2000:
        discount = total_amt * 0.05
    else:
        discount = 0
    return total_amt, discount

# print(bill_calc([900, 450, 670, 230]))


# === 2. Student Grade Calculator ===
def grade_calc(marks: list):
    total_marks = 0
    failed_sub = 0
    # Calculates total marks
    for mark in marks:
        total_marks += mark

        if mark < 40:
            failed_sub += 1

    # Calculates average
    avg = total_marks / len(marks)

    # Determines the grade
    if failed_sub > 0:
        grade = 'F'
        res = 'Fail'
    elif avg >= 90:
        grade = 'A'
        res = 'Pass'
    elif avg >= 80:
        grade = 'B'
        res = 'Pass'
    elif avg >= 70:
        grade = 'C'
        res = 'Pass'
    elif avg >= 60:
        grade = 'D'
        res = 'Pass'
    else:
        grade = 'E'
        res = 'Pass'

    print("Total Marks:", total_marks)
    print("Average:", avg)
    print("Grade:", grade)
    print("Result:", res)

# grade_calc([45, 78, 98, 45, 65])


# === 3. Employee Bonus Calculator ===
def bonus_calc(annual_sal, exp_yrs, score):
    if exp_yrs >= 5 and score >= 80:
        bonus = 0.15
    elif exp_yrs >= 3 and score >= 70:
        bonus = 0.10
    else:
        bonus = 0.05
    total_sal = annual_sal + bonus
    print(f"Bonus:{bonus}, Final Salary:{total_sal}")

# bonus_calc(700000, 4, 80)


# === 4. Parking Fee Calculator ===
def parking_fee_calc(hrs):
    if hrs <= 0:
        print("Invalid hours")
        return
    elif hrs <= 2:
        fee = hrs * 30
    elif 3 <= hrs <= 5:
        fee = (2 * 30) + ((hrs - 2) * 20)
    elif hrs > 5:
        fee = (2 * 30) + (3 * 20) + ((hrs - 5) * 15)
    print("Parking hours:", hrs)
    print("Parking fee:", fee)
    
# parking_fee_calc(4)
# parking_fee_calc(2)
# parking_fee_calc(7)


# === 5. Mobile Data Use Calculator ===
def mobile_data_use_calc(data_usage):
    charge = 0
    if data_usage < 2:
        print("No extra charges")
        charge = 0
    elif 2 <= data_usage <= 5:
        extra_data = data_usage - 2
        charge = extra_data * 20
    else:
        extra_data_first = 5 - 2
        extra_data_rem = data_usage - 5
        charge = (extra_data_first * 20) + (extra_data_rem * 30)
    print("Data used:", data_usage, "GB")
    print("Extra charge:", charge)
# mobile_data_use_calc(6)


# === 6. Electricity Bill Calculator ===
def elec_bill_calc(units):
    if units <= 0:
        print("Invalid units")
        return
    bill = 0
    for unit in range(1, units+1):
        if unit <= 100:
            bill += 2
        elif unit <= 200:
            bill += 3
        elif unit <= 300:
            bill += 5
        else:
            bill += 7
    print("Units consumed:", units)
    print("Electricity Bill:", bill)
# elec_bill_calc(250)


# === 7. Restaurant Billing System ===
def restaurant_bill():
    menu = {
        'pizza': 300,
        'burger': 150,
        'pasta': 200,
        'biryani': 250,
        'drinks': 80
    }
    total = 0
    while True:
        print("\nMenu:")
        print("Pizza - ₹300")
        print("Burger - ₹150")
        print("Pasta - ₹200")
        print("Biryani - ₹250")
        print("Drinks - ₹80")
        print("Type 'done' to finish")

        item = input("Enter item: ").lower()
        if item == "done":
            break

        if item in menu:
            quantity = int(input("Enter quantity: "))
            if quantity > 0:
                total += menu[item] * quantity
            else:
                print("Invalid quantity")
        else:
            print("Item not available")

    if total > 1500:
        discount = total * 0.10
    else:
        discount = 0
    final_amount = total - discount
    print("\nSubtotal:", total)
    print("Discount:", discount)
    print("Final amount:", final_amount)
# restaurant_bill()


# === 8. ATM Withdrawal ===
def atm_withdrawal(curr_bal):
    while True:
        print("\n1. Check Balance\n2. Withdraw\n3. Deposit\n4. Exit")
        ch = int(input("Enter your choice:"))
        if ch == 1:
            print("Current balance:", curr_bal)
        elif ch == 2:
            amt = float(input("Enter withdrawal amount:"))
            if amt <= 0:
                print("Invalid amount")
            elif amt > curr_bal:
                print("Insufficient balance")
            else:
                curr_bal -= amt
                print("Withdrawal successful")
                print("Remaining balance", curr_bal)
        elif ch == 3:
            amt = float(input("Enter deposited amount:"))
            if amt <= 0:
                print("Invalid amount")
            else:
                curr_bal += amt
                print("Deposit successful")
                print("Current balance:", curr_bal)
        elif ch == 4:
            print("Thank you for using the ATM")
            break
        else:
            print("Invalid choice")

# atm_withdrawal(45000)


# === 9. Bus Ticket Booking ===
def bus_booking(age, num_of_tickets):
    ticket_price = 200
    if age < 5:
        price_per_ticket = 0
    elif age <= 12:
        price_per_ticket = ticket_price * 0.50
    elif age <= 59:
        price_per_ticket = ticket_price 
    else:
        price_per_ticket = ticket_price * 0.70
    total = price_per_ticket * num_of_tickets
    print("Age:", age)
    print("Number of tickets:", num_of_tickets)
    print("Price per tickets:", price_per_ticket)
    print("Total amount:", total)

# bus_booking(45, 2) 