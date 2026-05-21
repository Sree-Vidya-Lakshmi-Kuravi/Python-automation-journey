## Student Management System

# view all students
# add students
# search students
# update student marks
# delete marks
# calculate average marks
# find topper
# save data


## VIEW ALL STUDENTS
def get_stud_data(path):

    with open(path) as f:
        t = f.readlines()
    t1 = []

    for i in t:
        w = i.split(',')
        t1.append({'name' : w[0].strip(), 'marks' : int(w[1].strip())})

    return t1


## GET MAXIMUM MARKS
def max_marks(d):
    high = d[0]['marks']

    for i in d:
        if i['marks'] > high:
            high = i['marks']

    return high


## FIND NAME WITH MARKS
def get_name_by_marks(d, m):
    details = []

    for i in d:
        if i['marks'] == m:
            details.append(i)
    return details


## ADD STUDENT DATA
def add_stud(path, name, marks):
    # name = input("Enter the name of student: ").strip()
    # marks = input(f"Enter the marks of {name}: ").strip()

    with open(path, 'a') as f:
        f.write(name + ', ' + marks + '\n')
    
    return name, marks


## SEARCH STUDENT
def search_stud(d, name):
    for i in d:
        if i['name'] == name:
            return i


## UPDATE THE MARKS
def update_marks(path, name, updated_marks):
    d = get_stud_data(path)  # converts the file into list of dictionaries
    us = 0  # stores the updated student

    for i in d:
        if i['name'] == name:
            i['marks'] = updated_marks
            us = i  # stores the updated dictionary

    with open(path, 'w') as f:
        for i in d:
            f.write(i['name'] + ',' + str(i['marks']) + '\n')

    return us  # returns the updated student record


## DELETE STUDENT
def delete_student(path, name):
    d = get_stud_data(path)
    ds = [] # stores the details of student to delete

    for i in d:
        if i['name'] == name:
            d.remove(i)
            ds = i 

    with open(path, 'w') as f:
        for i in d:
            f.write(i['name'] + ',' + str(i['marks']) + '\n')
    
    return ds


## CALCULATE AVERAGE MARKS
def average_marks(d):
    marks_sum = 0
    for i in d:
        marks_sum += i['marks']

    return round(marks_sum/len(d), 2)


## SAVE THE DATA
def save_data(path, d):
    with open(path, 'w') as f:
        for i in d:
            f.write(i['name'] + ',' + str(i['marks']) + '\n') 
    return d

# print(get_stud_data(path))
# print(max_marks(get_stud_data(path)))
# print(get_name_by_marks(get_stud_data(path), 90))
# print(add_stud(path))
# print(search_stud(get_stud_data(path), "pb"))
# print(update_marks(path, "bvns", 88))
# print(delete_student(path, "pb"))
# print(average_marks(get_stud_data(path)))

# d = get_stud_data(path)
# print(save_data(path, d))



while True:
    path = r'E:\Vidya Career\IT JOB\Repati Kosam\Week 2\Projects\day_8_students.txt'

    d = get_stud_data(path)

    print("--------------------------------------------- STUDENT MANAGEMENT SYSTEM ---------------------------------------------")

    print("""
    1. View all students
    2. Add student
    3. Search student
    4. Update student marks
    5. Delete student
    6. Calculate average marks
    7. Find topper
    8. Save data
    9. Exit""")

    ch = int(input("Enter your choice (1 - 9): "))

    if ch == 9:
        break


    elif ch == 1:
        print("-----------------")
        print("Student Name || Marks")
        print("-----------------")

        for i in d:
            print(i['name'], "=", i['marks'])


    elif ch == 2:
        name = input("Enter the name of student: ").strip()
        s = search_stud(d, name)

        if not s:
            marks = input(f"Enter the marks of {name}: ").strip()
            student = add_stud(path, name, marks)
            print(f"Student with name '{student[0]}' and marks '{student[1]}' has been added successfully")
        else:
            print(f"Student with name '{name}' already exists !!!")
            print("Try again with another name")

        
    elif ch == 3:
        name = input("Enter the name of the student you need to search for: ").strip()

        stud = search_stud(d, name)
        if stud:
            print('Name : ', stud['name'], '\n' + 'Marks : ', stud['marks'])
        else:
            print(f"No such student with name '{name}' found")


    elif ch == 4:
        name = input("Enter the student name: ")
        s = search_stud(d, name)

        if s:
            marks = input(f"Enter the marks of {name}: ").strip()
            stud = update_marks(path, name, marks)
            print(f"{stud['name']}'s marks updated to marks '{marks}' successfully")
        else:
            print(f"Student with name: {name} doesnot exist")
            print('Try again')

        
    elif ch == 5:
        name = input("Enter the student name you want to delete: ")
        s = search_stud(d, name)
        if s:
            stud = delete_student(path, name)
            print(f"Student with name {name} has been deleted successfully")
        else:
            print(f"Student with name {name} does not exist")

        
    elif ch == 6:
        if d:
            avg = average_marks(d)
            print(f"The average marks of the class is: {avg}")
        else:
            print("No student data found")


    elif ch == 7:
        ts = max_marks(d)
        students = get_name_by_marks(d, ts)

        if students:
            if len(students) == 1:
                print("The topper of the class is: ")
                print("Name: ", students[0]['name'])
                print("Marks: ", students[0]['marks'])

            else:
                print("The toppers of the class are: ")

                for i in students:
                    print("-----------------")
                    print("Name: ", i['name'])
                    print("Marks: ", i['marks'])
        else:
            print('No data found !!!!')

    elif ch == 8:
        if d:
            data = save_data(path, d)
            print("The data has been saved successfully in the file !!!")

        else:
            print("No data is found")


    else:
        print("Wrong Choice :(")







