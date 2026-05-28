### EMPLOYEE DATA MANAGER

import os
import csv
import json

path = r'E:\Vidya Career\IT JOB\Repati Kosam\Week_3\Projects\sample_files\employees.csv'

j_path = r'E:\Vidya Career\IT JOB\Repati Kosam\Week_3\Projects\sample_files\employees.json'


## Data loading
# csv data loading
def load_csv_f(path):
    with open(path, 'r') as f:
        reader = csv.DictReader(f)
        return list(reader), reader.fieldnames


# json data loading
def load_json_f(j_path):
    with open(j_path, 'r') as f:
        return json.load(f)



## Add Employee
# using csv
headers = ['name','department','salary']
file_exists = os.path.exists(path)
def add_emp_csv(path):
    with open(path, 'a', newline = '') as f:
        writer = csv.DictWriter(f, fieldnames = headers)

        if not file_exists:
            writer.writeheader()

        e_name = input("Enter employee name:")
        e_dept = input("Enter the emp department:")
        e_sal = int(input("Enter the emp salary:"))

        new_emp = {"name": e_name, "department": e_dept, "salary": e_sal}

        writer.writerow(new_emp)

    print("The data has been appended successfully")

# add_emp_csv(path)

# using json
def add_emp_json(j_path):
    with open(j_path, 'r+') as f:
        data = load_json_f(j_path)

        je_name = input("Enter employee name:")
        je_dept = input("Enter the emp department:")
        je_sal = int(input("Enter the emp salary:"))

        new_e = {"name":je_name,"department":je_dept,"salary":je_sal}
        
        data.append(new_e)
        json.dump(data, f, indent = 4)

    print("The data has been added successfully")

# add_emp_json(j_path)


## View Employees
# using csv
def view_emp_csv(path):
    with open(path, 'r') as f:
        reader = csv.DictReader(f)

        for row in reader:
            print("Name:", row['name'], '||', "Department:", row['department'], '||', "Salary:", row['salary'])

# view_emp_csv(path)

# using json
def view_emp_json(j_path):
    data = load_json_f(j_path)
    for i in data:
        print(i)

# view_emp_json(j_path)


## Search Employee
# using csv
def search_csv(path, emp_name):
    data = load_csv_f(path)
    for i in data:
        if i["name"].lower() == emp_name:
            return i
            
# print(search_csv(path, "mahi"))

# using json
def search_json(j_path, empName):
    d = load_json_f(j_path)

    for i in d:
        if i['name'] == empName:
            return i
    else:
        print("No such record found")

# print(search_json(j_path, "mahi"))


## Save to json - Converting csv file to json file
def save_to_json(path):
    data = load_csv_f(path)
    with open(path, 'w') as f:
        json.dump(data, f, indent = 4)
    print("CSV converted to JSON successfully")

# save_to_json(path)


## Export csv - read json and write csv
def export_csv(path, j_path):
    data = load_json_f(j_path)
    headers = ["name", "department", "salary"]
    with open(path, 'w', newline = '') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)

# export_csv(path, j_path)


while True:
    try:
        print("====================== EMPLOYEE DATA MANAGER ======================")
        print("1. Add new employee\n2. View all employees\n3. Search an employee\n4. Save to JSON\n5. Export to CSV\n6. Exit")

        ch = int(input("Enter your choice:"))

        if ch == 6:
            break

        elif ch == 1:
            print("------------------------------------------------------")
            print("1. Add employee in CSV\n2. Add employee in JSON\n0. Exit")

            a = int(input("Enter how where you want to add employee:"))

            if a == 3:
                break

            elif a == 1:
                add_emp_csv(path)

            elif a == 2:
                add_emp_json(j_path)
            
            else:
                print("Wrong Choice.. Select between (0/1/2)")

        
        elif ch == 2:
            print("------------------------------------------------------")
            print("1. View employee in CSV\n2. View employee in JSON\n0. Exit")

            a = int(input("Enter how where you want to add employee:"))

            if a == 3:
                break

            elif a == 1:
                view_emp_csv(path)

            elif a == 2:
                view_emp_json(j_path)
            
            else:
                print("Wrong Choice.. Select between (0/1/2)")


        elif ch == 3:
            print("------------------------------------------------------")
            print("1. Search employee in CSV\n2. Search employee in JSON\n0. Exit")

            a = int(input("Enter how where you want to add employee:"))

            if a == 3:
                break

            elif a == 1:
                emp_name = input("Enter the employee you want to search for:")
                search_csv(path, emp_name)

            elif a == 2:
                emp_name = input("Enter the employee you want to search for:")
                search_json(j_path, emp_name)
            
            else:
                print("Wrong Choice.. Select between (0/1/2)")

        
        elif ch == 4:
            save_to_json(path)

        
        elif ch == 5:
            export_csv(path, j_path)

        
        else:
            print("Wrong choice. Select correct choice (1/2/3/4/5/6)")

    except FileNotFoundError:
        print("No such file found")

    except ValueError:
        print("The choices should be in integer only")

