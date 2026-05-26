from student_manager import StudentManager


path = 'data/students.txt'
while True:
    stud_man = StudentManager(path)
    print("""--------------------------------------------------------------------------------------
------------------------------- Student Management System ----------------------------
--------------------------------------------------------------------------------------
          1. View all students
          2. Add student
          3. Search student
          4. Update student marks
          5. Delete student
          6. calculate average marks
          7. Find Topper
          8. Save data
          0. Exit""")
    try:
        c = int(input("Enter your choice(0-8) : "))

        if c == 0:
            break

        elif c == 1:
            stud_man.view_studs()

        elif c == 2:
            name = input("Enter the student's name : ").strip()
            marks = int(input("Enter the marks :"))
            stud_man.add_student(name, marks)

        elif c == 3:
            name = input("Enter the name of the student you want to search : ").strip()
            stud = stud_man.search_student(name)
            if stud:
                print('Name :', stud['name'], '\n'+'Marks :', stud['marks'])
            else:
                print(f"No student found with name : {name}")


        elif c == 4:
            name = input("Enter the student name : ")
            s = stud_man.search_student(name)
            if s:
                marks = input(f"Enter the marks of {name} : ").strip()
                stud = stud_man.update_marks(name, marks)
                print(f"'{name}'s' marks updated to marks : '{marks}' successfully")
            else:
                print(f"Student with name : '{name}' not exists !!!")
                print('Try again !!')


        elif c == 5:
            name = input("Enter the student name you want to delete : ")
            s = stud_man.search_student(name)
            if s:
                stud = stud_man.delete_stud(name)
                print(f"Student with name : '{name}' deleted successfully")
            else:
                print(f"Student with name : '{name}' not exists !!!!")


        elif c == 6:
            stud_man.get_avg()

        elif c == 7:
            stud_man.get_topper()

        elif c == 8:
            stud_man.save_data()

    except ValueError:
        print("The choice must be an integer")