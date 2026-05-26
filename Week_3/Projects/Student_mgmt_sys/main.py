
from student_manager import StudentManager

path = 'data/students.txt'

try:
    while True:

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

        try:
            stu_m = StudentManager(path)

            ch = int(input("Enter your choice (1 - 9): "))

            if ch == 9:
                break


            elif ch == 1:
                stu_m.view_studs()
                

            elif ch == 2:
                try:
                    name = input("Enter the name of student: ").strip()
                    marks = input(f"Enter the marks of {name}: ").strip()
                    stu_m.add_student(name, marks)

                except ValueError:
                    print("The marks must be integer value only.")

                
            elif ch == 3:
                name = input("Enter the name of the student you need to search for: ").strip()
                stud = stu_m.search_stu(name)
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


        except ValueError:
            print("The choice must be in integer only")

finally:
    print("The program has been terminated successfully.")