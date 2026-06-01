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
            data.append({'ename' : t[0].strip(), 'examt' : float(t[1].strip())})

    return data


## View all expenses
def view_expenses(data):
    print("-------------------------------------------")
    print("Expenses Data")
    print("-------------------------------------------")
    print("Expense Name - Expense Amount")
    print("-------------------------------------------")

    for i in data:
        print(i['ename'], '-', i['examt'])

    return data


## Add expense
def add_expense(path, d, e_name, e_amt):
    d.append({"ename": e_name, 'examt': float(e_amt)})

    with open(path, 'a') as f:
        f.write(e_name.capitalize() + ' - ' + str(e_amt) + '\n')
    
    return e_name, e_amt


## Calculate all expenses
def calc_all_expenses(data):
    total = 0

    for i in data:
        total += i['examt']

    return round(total, 2)


## Search expense by name
def search_exp_by_name(data, name):
    # name = input("Enter the expense name you need to search for: ")

    for i in data:
        if i['ename'].lower() == name:
            return i


## Delete expenses
def del_expense_by_name(data, name):
    delete = {}

    for i in data:
        if i['ename'].lower() == name:
            data.remove(i)
            delete = i

    with open(path, 'w') as f:
        for i in data:
            f.write(i["ename"] + " - " + str(i["examt"]) + '\n')

    return delete


## Filter expense by amount
def filter_data_desc(data):
    fd = data

    for i in range(len(fd)):
        for j in range(i+1, len(fd)):
            if fd[i]['examt'] < fd[j]['examt']:
                fd[i], fd[j] = fd[j], fd[i]
    return fd


def filter_data_asc(data):
    fd = data

    for i in range(len(fd)):
        for j in range(i+1, len(fd)):
            if fd[i]['examt'] > fd[j]['examt']:
                fd[i], fd[j] = fd[j], fd[i]
    return fd


## Filtering the data
def filter_above_range(data, r):
    fil_data = []
    for i in data:
        if i['examt'] >= r:
            fil_data.append(i)
    return fil_data


def filter_below_range(data, r):
    fil_data = []
    for i in data:
        if i['examt'] <= r:
            fil_data.append(i)
    return fil_data


## Save expenses to a file
def save_file(path, data):
    with open(path, 'w') as f:
        for i in data:
            f.write(i["ename"] + ' - ' + str(i['examt']) + '\n')
    

# print(fetch_data(path))
# print(add_expense(path))
# print(calc_all_expenses(fetch_data(path)))
# print(search_exp_by_name(fetch_data(path), "Groceries"))
# print(del_expense_by_name(fetch_data(path), "Gym Membership"))
# print(filter_exp_by_amt(fetch_data(path), 2500))
# print(save_file(fetch_data(path)))


while True:
    try:
        path = r'E:\Vidya Career\IT JOB\Repati Kosam\Week 2\Projects\day_9_expenses.txt'

        data = fetch_data(path)

    

        print("================== EXPENSE TRACKER ==================")
        print("1. Add expense\n2. View all expenses\n3. Calculate all the expenses\n4. Search expense by name\n5. Delete expense\n6. Filter expense by amount\n7. Save expenses\n8. Exit")


        try:
            ch = int(input("Enter the choice (1 - 8): "))

            if ch == 8:
                break


            elif ch == 1:
                try:
                    name = input("Enter your expense name: ").strip().lower()
                    s = search_exp_by_name(data, name)
                    if s:
                        print("Expense Name already exists!!")

                    else:
                        amt = float(input("Enter the expense amount: "))
                        new_exp = add_expense(path, data, name, amt)
                        print(f"Expense Name: {new_exp[0]} - Expense Amount: {new_exp[1]}")
                        print("Expense has been added successfully")

                except ValueError:
                    print("The amount must be numerics only")
                

            elif ch == 2:
                print(view_expenses(data))


            elif ch == 3:
                print(view_expenses(data))
                t = calc_all_expenses(data)
                print('-------------------------------------------------------')
                print("The total amount of all the expenses is: ", t)
                print('-------------------------------------------------------')


            elif ch == 4:
                name = input("Enter the expense name you want to search: ")
                s = search_exp_by_name(data, name)
                if s:
                    print("The searched expense is: ")
                    print(f"Expense name: {s['ename']} - {s['examt']}")
                else:
                    print("Expense not found !!")


            elif ch == 5:
                name = input("Enter the expense name you want to delete: ").strip().lower()
                s = search_exp_by_name(data, name)
                if s:
                    d = del_expense_by_name(data, name)
                    print("Expense has been deleted successfully !!")
                    print("The Expense details are: ")
                    print(f"Expense name: {d['ename']} - Expense Amount: {d['examt']}")

                else:
                    print(f"No expense found with the name: '{name}'")


            elif ch == 6:
                print("1. Sort from HIGH to LOW")
                print("2. Sort from LOW to HIGH")
                print("3. Sort the data above the given range of amount")
                print("4. Sort the data below the given range of amount")

                try:
                    c1 = int(input("Enter your choice for filtering :"))
                    
                    if c1 == 1:
                        fd = filter_data_desc(data)
                        print("Sorted the data from high to low")
                        print(view_expenses(fd))

                    elif c1 == 2:
                        fd = filter_data_asc(data)
                        print("Sorted the data from low to High")
                        print(view_expenses(fd))

                    elif c1 == 3:
                        try:
                            r = float(input("Enter the range of amount:"))
                            print(f"The Expenses with amount greater than or equal to '{r}'")
                            fd = filter_above_range(data, r)
                            print(view_expenses(fd))

                        except ValueError:
                            print("The range must be integer or decimal only")

                    elif c1 == 4:
                        try:
                            r = float(input("Enter the range of amount:"))
                            print(f"The Expenses with amount Less than or equal to '{r}'")
                            fd = filter_below_range(data, r)
                            print(view_expenses(fd))

                        except ValueError:
                            print("The range must be integer or decimal only")

                    else:
                        print('Invalid Choice !!')

                except ValueError:
                    print("The choice must be in integer only")


            elif ch == 7:
                if data:
                    save_file(path, data)
                    print("Data saved successfully !!!")
                else:
                    print("No data found to be saved !!")

            else:
                print("Wrong Choice !! Select between the choices 1 - 8")


        except ValueError:
            print("The choice must be an integer")

    except FileNotFoundError:
        print("File not found")
        break

    finally:
        print("The program has been terminated successfully")
        break