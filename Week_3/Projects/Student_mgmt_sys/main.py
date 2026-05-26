
from student_manager import StudentManager

path = 'data/students.txt'

try:
    while True:
        stu_m = StudentManager(path)
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

            ch = int(input("Enter your choice (1 - 9): "))

            if ch == 9:
                break


            elif ch == 1:
                stu_m.view_studs()
                

            elif ch == 2:
                try:
                    name = input("Enter the name of student: ").strip()
                    marks = int(input(f"Enter the marks of {name}: "))
                    stu_m.add_student(name, marks)

                except ValueError:
                    print("The marks must be integer value only.")

                
            elif ch == 3:
                name = input("Enter the name of the student you need to search for: ").strip()
                stud = stu_m.search_stu(name)
                if stud:
                    print('The student has been found successfully')
                    print("Name: ", stud['name'])
                    print("Marks: ", stud['marks'])

                else:
                    print(f"No such student with name '{name}' found")


            elif ch == 4:
                name = input("Enter the student name: ")
                s = stu_m.search_stu(name)

                if s:
                    marks = input(f"Enter the marks of {name}: ").strip()
                    stud = stu_m.update_mar(name, marks)
                    print(f"{name}'s marks updated to marks '{marks}' successfully")
                else:
                    print(f"Student with name: {name} doesnot exist")
                    print('Try again')

                
            elif ch == 5:
                name = input("Enter the student name you want to delete: ")
                s = stu_m.search_stu(name)
                if s:
                    stud = stu_m.delete_stud(name)
                    print(f"Student with name {name} has been deleted successfully")
                else:
                    print(f"Student with name {name} does not exist")

                
            elif ch == 6:
                stu_m.get_avg()


            elif ch == 7:
                stu_m.get_topper()


            elif ch == 8:
                stu_m.save_data()

            else:
                print("Wrong Choice :(")


        except ValueError:
            print("The choice must be in integer only")

finally:
    print("The program has been terminated successfully.")