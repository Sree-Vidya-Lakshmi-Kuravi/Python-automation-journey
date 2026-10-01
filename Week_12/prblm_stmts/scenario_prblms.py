# === 1. Bank Account & Daily Transaction System ===
def bank_sys(initial_bal):
    curr_bal = initial_bal
    transactions = []
    while True:
        print("===== BANK SYSTEM =====")
        print("\n1. Check Balance\n2. Deposit Money\n3. Withdraw Money\n4. View Transaction Summary\n5. Exit")
        ch = int(input("Enter your choice:"))

        if ch == 1:
            print("Current Balance:", curr_bal)

        elif ch == 2:
            amt_to_deposit = float(input("Enter the amount to be deposited:"))
            if amt_to_deposit < 0:
                print("Invalid deposit amount")
                break
            curr_bal += amt_to_deposit
            transactions.append(['Deposit', amt_to_deposit])
            print("Deposit successful..")
            print("Current Balance:", curr_bal)
            
        elif ch == 3:
            amt_to_withdraw = float(input("Enter the amount to withdraw:"))
            if amt_to_withdraw < 0:
                print("Invalid amount to withdraw")
                break
            if amt_to_withdraw > curr_bal:
                print("Insufficient balance")
                break
            if amt_to_withdraw == 10000:
                print("Cannot withdraw the amount greater than 10000 in single transaction")
                break
            else:
                curr_bal -= amt_to_withdraw
                transactions.append(['Deposit', amt_to_withdraw])
                print("Withdraw successful..")
                print("Remaining Balance:", curr_bal)

        elif ch == 4:
            total_deposit = total_withdraw = 0
            for t in transactions:
                transaction_type = t[0]
                amt = t[1]
                if transaction_type == "Deposit":
                    total_deposit += amt
                elif transaction_type == "Withdraw":
                    total_withdraw += amt
            print("-- Transaction Summary --")
            print("Number of transactions:", len(transactions))
            print("Total Deposited:", total_deposit)
            print("Total Withdrawal:", total_withdraw)   

        elif ch == 5:
            print("Thank you.. Visit again :)")
            break
# bank_sys(59000)


# === 2. Supermarket Checkout & Discount System ===
def supermarket():
    products = {
        "rice": 60,
        "sugar": 50,
        "milk": 30,
        "bread": 45,
        "eggs": 70,
        "oil": 150,
        "biscuits": 30
    }
    cart = []
    while True:
        print("\n========== SUPERMARKET ==========")
        print("Rice      ₹60")
        print("Sugar     ₹50")
        print("Milk      ₹30")
        print("Bread     ₹45")
        print("Eggs      ₹70")
        print("Oil       ₹150")
        print("Biscuits  ₹30")
        print("\nType 'done' when you have finished shopping.")
        item = input("Enter product: ").lower()
        if item == "done":
            break
        if item not in products:
            print("Product not available.")
            continue
        quantity = int(input("Enter quantity: "))
        if quantity <= 0:
            print("Invalid quantity.")
            continue
        price = products[item]
        total = price * quantity
        cart.append([item, quantity, price, total])
        print("Item added to cart.")

    # Check whether cart is empty
    if len(cart) == 0:
        print("\nNo items purchased.")
        return

    # Calculate subtotal
    subtotal = 0
    for item in cart:
        subtotal += item[3]
    # Calculate discount
    if subtotal < 1000:
        discount_percentage = 0
    elif subtotal < 2500:
        discount_percentage = 5
    elif subtotal < 5000:
        discount_percentage = 10
    else:
        discount_percentage = 15
    discount = subtotal * discount_percentage / 100
    amount_after_discount = subtotal - discount

    # GST
    gst = amount_after_discount * 5 / 100
    final_amount = amount_after_discount + gst
    # Find most expensive item
    most_expensive_item = cart[0]
    for item in cart:
        if item[3] > most_expensive_item[3]:
            most_expensive_item = item

    # Total quantity
    total_quantity = 0
    for item in cart:
        total_quantity += item[1]

    # Print bill
    print("\n========== FINAL BILL ==========")
    print("\nProduct\t\tQty\tPrice\tTotal")
    print("----------------------------------------")

    for item in cart:
        name = item[0]
        quantity = item[1]
        price = item[2]
        total = item[3]
        print(name, "\t\t", quantity, "\t₹", price, "\t₹", total)

    print("----------------------------------------")
    print("Subtotal:", subtotal)
    print("Discount:", discount)
    print("Amount after discount:", amount_after_discount)
    print("GST (5%):", gst)
    print("----------------------------------------")
    print("FINAL AMOUNT:", final_amount)
    print("\nNumber of different products:", len(cart))
    print("Total quantity of items:", total_quantity)
    print("Highest purchase:", most_expensive_item[0])
    print("\nThank you for shopping!")

# supermarket()


# === 3. Hospital Patient Billing System ===
def hospital_billing_sys():
    rooms = {
        "general": 1000,
        "semi-private": 2000,
        "private": 4000
    }
    doctors = {
        "general doctor": 500,
        "specialist": 1000,
        "senior specialist": 1500
    }
    medicines = {
        "paracetamol": 5,
        "antibiotic": 20,
        "vitamin": 10,
        "painkiller": 15,
        "syrup": 50
    }

    print("\n========== PATIENT DETAILS ==========")
    patient_name = input("Enter patient name: ")
    age = int(input("Enter patient age: "))
    days = int(input("Enter number of days admitted: "))

    if age <= 0:
        print("Invalid age.")
        return
    if days <= 0:
        print("Invalid number of days.")
        return

    print("\n========== ROOM TYPES ==========")
    print("General        - ₹1000/day")
    print("Semi-Private   - ₹2000/day")
    print("Private        - ₹4000/day")
    room_type = input("Enter room type: ").lower()
    if room_type not in rooms:
        print("Invalid room type.")
        return
    room_price = rooms[room_type]
    room_charges = room_price * days

    print("\n========== DOCTOR TYPES ==========")
    print("General Doctor      - ₹500")
    print("Specialist          - ₹1000")
    print("Senior Specialist   - ₹1500")
    print("\nPatient can select multiple consultations.")
    print("Type 'done' when finished.")

    consultations = []
    while True:
        doctor_type = input("Enter doctor type: ").lower()
        if doctor_type == "done":
            break
        if doctor_type not in doctors:
            print("Invalid doctor type.")
            continue
        consultations.append(doctor_type)
        print("Consultation added.")

    doctor_charges = 0
    for doctor in consultations:
        doctor_charges += doctors[doctor]

    print("\n========== MEDICINES ==========")
    print("Paracetamol  - ₹5")
    print("Antibiotic   - ₹20")
    print("Vitamin      - ₹10")
    print("Painkiller   - ₹15")
    print("Syrup        - ₹50")
    print("\nEnter 'done' when finished.")

    medicine_list = []
    while True:
        medicine = input("Enter medicine: ").lower()
        if medicine == "done":
            break
        if medicine not in medicines:
            print("Medicine not available.")
            continue

        quantity = int(input("Enter quantity: "))
        if quantity <= 0:
            print("Invalid quantity.")
            continue

        price = medicines[medicine]
        total = price * quantity
        medicine_list.append([medicine, quantity, price, total])

        print("Medicine added.")

    medicine_charges = 0
    for medicine in medicine_list:
        total = medicine[3]
        medicine_charges += total
    subtotal = (room_charges + doctor_charges + medicine_charges)

    print("\n========== INSURANCE ==========")
    insurance = input("Does the patient have insurance? (yes/no): ").lower()
    if insurance == "yes":
        if subtotal < 50000:
            insurance_coverage = subtotal * 20 / 100
        else:
            insurance_coverage = subtotal * 30 / 100
    elif insurance == "no":
        insurance_coverage = 0
    else:
        print("Invalid insurance option.")
        return
    final_bill = subtotal - insurance_coverage

    print("\n")
    print("============================================")
    print("              HOSPITAL BILL")
    print("============================================")

    print("\nPATIENT DETAILS")
    print("--------------------------------------------")
    print("Patient Name      :", patient_name)
    print("Age               :", age)
    print("Days Admitted     :", days)
    print("Room Type         :", room_type.title())
    print("\nROOM CHARGES")
    print("--------------------------------------------")
    print("Room Price/Day    : ₹", room_price)
    print("Number of Days    :", days)
    print("Room Charges      : ₹", room_charges)
    print("\nDOCTOR CONSULTATIONS")
    print("--------------------------------------------")
    if len(consultations) == 0:
        print("No consultations selected.")
    else:
        for doctor in consultations:
            print(
                doctor.title(),
                ":", 
                "₹",
                doctors[doctor]
            )

    print("Doctor Charges    : ₹", doctor_charges)

    print("\nMEDICINE DETAILS")
    print("--------------------------------------------")
    if len(medicine_list) == 0:
        print("No medicines purchased.")
    else:
        for medicine in medicine_list:
            name = medicine[0]
            quantity = medicine[1]
            price = medicine[2]
            total = medicine[3]
            print(
                name.title(),
                "| Quantity:",
                quantity,
                "| Price: ₹",
                price,
                "| Total: ₹",
                total)
    print("Medicine Charges  : ₹", medicine_charges)
    print("\nBILL SUMMARY")
    print("--------------------------------------------")
    print("Room Charges      : ₹", room_charges)
    print("Doctor Charges    : ₹", doctor_charges)
    print("Medicine Charges  : ₹", medicine_charges)
    print("--------------------------------------------")
    print("Subtotal          : ₹", subtotal)
    print("Insurance Cover   : ₹", insurance_coverage)
    print("--------------------------------------------")
    print("FINAL BILL        : ₹", final_bill)
    print("============================================")
    print("          Thank you.")
    print("============================================")

hospital_billing_sys()