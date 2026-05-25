## Student Management System using OOPS

# view all students
# add students
# search students
# update student marks
# delete marks
# calculate average marks
# find topper
# save data

class StudentMgmt:
    class Student:
        def __init__(self, name, marks):
            self.name = name
            self.marks = marks

        def get_name(self):
            return self.name

        def get_marks(self):
            return self.marks

        def set_marks(self, u_marks):
            self.marks = u_marks

    # From here, the data comes under StudentMgmt class

    students = [Student("Alice", 85),
                Student("Bob", 80),
                Student("Clara", 70),
                Student("Diana", 60),
                Student("Fiama", 60),
                Student("George", 20),
                Student("Harry", 50),
                Student("Ivana", 30),
                Student("Mahi", 99)]

    def get_stud(self):
        return self.students

    def add_student(self, name, marks):
        self.students.append(self.Student(name, marks))
        print("Student has been added successfully")

    def view_students(self):
        for i in self.students:
            print(i.get_name(), ':', i.get_marks())

    def update_stu_marks(self, name, marks):
        for i in self.students:
            if i.get_name() == name:
                i.set_marks(marks)
                break

    def delete_student(self, name):
        for i in self.students:
            if i.get_name() == name:
                self.students.remove(i)
                break


sm = StudentMgmt()
sm.add_student('BVNS', 89)
sm.view_students()
print('------------------------')
sm.add_student('PB', 78)
sm.view_students()
print('------------------------')
sm.delete_student('PB')
sm.view_students()
print('------------------------')
sm.update_stu_marks('Mahi', 100)
sm.view_students()
