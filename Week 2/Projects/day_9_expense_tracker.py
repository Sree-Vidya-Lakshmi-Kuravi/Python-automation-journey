## EXPENSE TRACKER

# Add expense
# View all expenses
# Calculate all expenses
# Search expense by name
# Delete expense
# Filter expense by amount
# Save expenses to file
# Menu based system


def fetch_data(path):
    data = []

    with open(path) as f:
        for line in f:
            t = line.strip().split(' - ')
            data.append({'Expense Name' : t[0].strip(), 'Expense Amount' : float(t[1].strip())})

    return data


## View all expenses
def view_expenses(data):
    print("-------------------------------------------")
    print("Expenses Data")
    print("-------------------------------------------")
    print("Expense Name - Expense Amount")
    print("-------------------------------------------")

    for i in data:
        print(i['Expense Name'], '-', i['Expense Amount'])

    return data


## Add expense
def add_expense(path, d, e_name, e_amt):
    d.append({"Expense Name": e_name, 'Expense Amount': float(e_amt)})

    with open(path, 'a') as f:
        f.write(e_name.capitalize() + ' - ' + str(e_amt) + '\n')
    
    return e_name, e_amt


## Calculate all expenses
def calc_all_expenses(data):
    total = 0

    for i in data:
        total += i['Expense Amount']

    return round(total, 2)


## Search expense by name
def search_exp_by_name(data, name):
    # name = input("Enter the expense name you need to search for: ")

    for i in data:
        if i['Expense Name'].lower() == name:
            return i


## Delete expenses
def del_expense_by_name(data, name):
    delete = {}

    for i in data:
        if i['Expense Name'].lower() == name:
            data.remove(i)
            delete = i

    with open(path, 'w') as f:
        for i in data:
            f.write(i["Expense Name"] + " - " + str(i["Expense Amount"]) + '\n')

    return delete


## Filter expense by amount
def filter_data_desc(data):
    filter_data = data

    for i in range(len(filter_data)):
        for j in range(i+1, len(filter_data)):
            if filter_data[i]['Expense Amount'] < filter_data[j]['Expense Amount']:
                filter_data[i], filter_data[j] = filter_data[j], filter_data[i]
    return filter_data


def filter_data_asc(data):
    filter_data = data

    for i in range(len(filter_data)):
        for j in range(i+1, len(filter_data)):
            if filter_data[i]['Expense Amount'] > filter_data[j]['Expense Amount']:
                filter_data[i], filter_data[j] = filter_data[j], filter_data[i]
    return filter_data


## Filtering the data
def filter_above_range(data, r):
    fil_data = []
    for i in data:
        if i['Expense Amount'] >= r:
            fil_data.append(i)
    return fil_data


def filter_above_range(data, r):
    fil_data = []
    for i in data:
        if i['Expense Amount'] <= r:
            fil_data.append(i)
    return fil_data


## Save expenses to a file
def save_file(path, data):
    with open(path, 'w') as f:
        for i in data:
            f.write(i["Expense Name"] + ' - ' + str(i['Expense Amount']) + '\n')
    

# print(fetch_data(path))
# print(add_expense(path))
# print(calc_all_expenses(fetch_data(path)))
# print(search_exp_by_name(fetch_data(path), "Groceries"))
# print(del_expense_by_name(fetch_data(path), "Gym Membership"))
# print(filter_exp_by_amt(fetch_data(path), 2500))
# print(save_file(fetch_data(path)))


while True:
    path = 'E:\\Vidya Career\\IT JOB\\Repati Kosam\\rk_Projects\\day_9_expenses.txt'

    data = fetch_data(path)

    print("================== EXPENSE TRACKER ==================")
    print("1. Add expense\n2. View all expenses\n3. Calculate all the expenses\n4. Search expense by name\n 5. Delete expense\n6. Filter expense by amount\n7. Save expenses\n8. Exit")

    ch = int(input("Enter the choice: "))

    if ch == 8:
        break


    elif ch == 1:
        name = input("Enter your expense name: ")
        s = search_exp_by_name(data, name)
        if s:
            print("Expense Name already exists!!")

        else:
            amt = float(input("Enter the expense amount: "))
            new_exp = add_expense(path, data, name, amt)
            print(f"Expense Name: {new_exp[0]} - Expense Amount: {new_exp[1]}")
            print("Expense has been added successfully")
        

    elif ch == 2:
        view_expenses(data)

    elif ch == 3:
        view_expenses(data)
        t = calc_all_expenses(data)
        print('-------------------------------------------------------')
        print("The total amount of all the expenses is: ", t)
        print('-------------------------------------------------------')


    elif ch == 4:
        name = input("Enter the expense name you want to search: ")
        s = search_exp_by_name(data, name)
        if s:
            print("The searched expense is: ")
            print(f"Expense name: {s['Expense Name']} - {s['Expense Amount']}")
        else:
            print("Expense not found !!")


    elif ch == 5:
        name = input("Enter the expense name you want to delete: ").strip().lower()
        s = search_exp_by_name(data, name)
        if s:
            d = del_expense_by_name(data, name)
            print("Expense has been deleted successfully !!")
            print("The Expense details are: ")
            print(f"Expense name: {d['Expense Name']} - Expense Amount: {d['Expense Amount']}")

            print(f"No expense found with the name: '{name}'")


    elif ch == 6:
        print("1. Sort from HIGH to LOW")
        print("2. Sort from LOW to HIGH")
        print("3. Sort the data above given range of amount")
        print("4. Sort the data below given range of amount")
        c1 = int(input("Enter your choice for filtering :"))
        
        if c1 == 1:
            sd = filter_data_desc(data)
            print("Sorted data from High to low")
            view_data(sd)

        elif c1 == 2:
            sd = filter_data_asc(data)
            print("Sorted data from Low to High")
            view_data(sd)

        elif c1 == 3:
            r = float(input("Enter the range of amount :"))
            print(f"The Expenses with amount greater than or equal to '{r}'")
            sd = filter_above_range(data, r)
            view_data(sd)

        elif c1 == 4:
            r = float(input("Enter the range of amount :"))
            print(f"The Expenses with amount Less than or equal to '{r}'")
            sd = filter_below_range(data, r)
            view_data(sd)

        else:
            print('Invalid Choice !!')


    elif ch == 7:
        if data:
            save_data(path, data)
            print("Data saved successfully !!!")
        else:
            print("No data found to be saved !!")

    else:
        print("Wrong Choice !! Select between the choices 1 - 8")
