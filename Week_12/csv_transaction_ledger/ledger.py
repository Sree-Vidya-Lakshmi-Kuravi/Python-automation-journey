import csv
import os

filename = os.path.join('csv_transaction_ledger', 'expenses.csv')

def ensure_file_exists(file_path):
    folder = os.path.dirname(file_path)
    if folder and not os.path.exists(folder):
        os.makedirs(folder)

    if not os.path.exists(file_path):
        with open(file_path, 'w', newline = '') as f:
            writer = csv.DictWriter(f, fieldnames=['Date', 'Category', 'Amount'])
            writer.writeheader()

# Level 1: View Transactions
def view_transactions(file_path):
    try:
        with open(file_path, 'r') as f:
            reader = csv.DictReader(f)
            print("\n -- All Transactions -- ")
            for row in reader:
                print(f"Date: {row['Date']}| Category: {row['Category']}| Amount: {row['Amount']}")
    except FileNotFoundError:
        ensure_file_exists(file_path)
        print("\nNo ledger found. New file created..")

# Level 2: Add Transaction
def add_transaction(file_path):
    date = input("Enter the date in format (YYYY-MM-DD): ").strip()
    category = input("Enter the category: ").strip().title()

    if not date or not category:
        print("Error: 'Date' and 'Category' columns are empty.")
        return

    try:
        amount = float(input("Enter the amount: "))
        if amount <= 0:
            print("Invalid amount..")
            return 
        
    except ValueError:
        print("Enter the correct value..")
        return 

    fieldnames = ['Date', 'Category', 'Amount']
    data = {'Date': date, 'Category': category, 'Amount': f"{amount:.2f}"}
    with open(filename, 'a', newline = '') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow(data)
    print("New transaction has been added successfully")

# Level 3: Category Summary
def category_summary(file_path):
    try:
        budget = float(input("Enter the budget threshold: "))
        if budget <= 0:
            print("Error: Budget threshold must be greater than zero.")
    except ValueError:
        print("Budget should always be positive.")
        return 

    category_totals = {}
    try:
        with open(filename, 'r') as f:
            reader = csv.DictReader(f)
            for r in reader:
                categ = r['Category']
                amt = r['Amount']
                category_totals[categ] = category_totals.get(categ, 0.0) + amt 
    except FileNotFoundError:
        ensure_file_exists()
        print("Ledger file does not exist. A new empty ledger has been created.")

    if not category_totals:
        print("No categories found to summarize.")
        return

    print("\n -- Category Summary -- ")
    for c, t in category_totals.items():
        print(f"-{c}: ${t:.2f}")

    print("\n -- Budget Alert -- ")
    bud_exceed = False
    for c, t in category_totals.items():
        if t > budget:
            amt_exceed = t - budget
            print(f" WARNING: Category {c} exceeded budget by {amt_exceed}!!!")
            bud_exceed = True

    if not bud_exceed:
        print("All categories are within budget") 
    
## ==== WORK FLOW ====
def main():
    ensure_file_exists(filename)

    while True:
        print("\n===== TRANSACTION LEDGER =====")
        print("1. View Transactions")
        print("2. Add New Transaction")
        print("3. Category Summary & Budget")
        print("4. Exit")

        ch = input("Enter your choice (1/2/3/4): ")

        if ch == '1':
            view_transactions(filename)
        elif ch == '2':
            add_transaction(filename)
        elif ch == '3':
            category_summary(filename)
        elif ch == '4':
            print("Exiting the transaction ledger..")
            break
        else:
            print("Invalid Selection. Select the correct choice (1/2/3/4)")

if __name__ == '__main__':
    main()