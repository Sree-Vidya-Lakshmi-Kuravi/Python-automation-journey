### CSV Handling

import os
import csv

path = 'day_17_sample.csv'
# creating a csv file 
def create_csv_w(path):
    with open(path, 'w', newline = '') as f:
        writer = csv.writer(f)
        writer.writerow(['id','name','marks'])

        for i in range(5):
            s_id = int(input("Enter the student id: "))
            s_name = input("Enter the student name: ")
            s_marks = int(input("Enter the marks: "))

            writer.writerow([s_id,s_name,s_marks])
    print("The csv file has been created successfully")

# create_csv_r(path)

headers = ['id','name','marks']
def create_csv_dw(path):
    with open(path, 'w', newline = '') as f:
        writer = csv.DictWriter(f, fieldnames = headers)
        writer.writeheader()

        for i in range(5):
            s_id = int(input("Enter the student id: "))
            s_name = input("Enter the student name: ")
            s_marks = int(input("Enter the marks: "))

            writer.writerow({'id': s_id, 'name': s_name, 'marks': s_marks})
    print("The csv file has been created successfully")


# read csv data
def read_csv_r(path):
    with open(path, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)   # prints data as a list

def read_csv_dr(path):
    with open(path, 'r+') as f:
        reader = csv.DictReader(f)
        for row in reader:
            print("Name:", row['name'])
            print("Marks:", row['marks'])  # prints data as dictionary

# calcualate the average
def avg_marks():
    total = 0
    count = 0

    with open('day_17_sample.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            total += int(row['marks'])
            count += 1
            avg = total/count

        print("Average:", avg)

# avg_marks()

def search_stu_by_name(path, name):
    with open(path, 'r') as f:
        reader = csv.DictReader(f)

        for row in reader:
            if row['name'] == name:
                return row
            else:
                print("No such student")

# print(search_stu_by_name(path, 'siri'))

# Add student
headers = ['id','name','marks']
file_exists = os.path.exists(path)
def create_csv_dw(path):
    with open(path, 'a', newline = '') as f:
        writer = csv.DictWriter(f, fieldnames = headers)
        
        if not file_exists:
            writer.writeheader()
        
        s_id = int(input("Enter the student id: "))
        s_name = input("Enter the student name: ")  
        s_marks = int(input("Enter the marks: "))

        writer.writerow({'id': s_id, 'name': s_name, 'marks': s_marks})

    print("The student has been added successfully")

create_csv_dw(path)
