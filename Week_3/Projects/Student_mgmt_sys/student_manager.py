from file_handler import *
from utils import *

class StudentManager:
    
    def __init__(self, path):
        self.path = path
        self.data = get_stud_data(path)


    def view_studs(self):
        print('---------------------')
        print('Student Data')
        print('---------------------')
        for i in self.data:
            print(i.get('name'), ':', i.get('marks'))



    def get_avg(self):
        avg = average_marks(self.data)
        print("The average marks of the students:", avg)

    
    def add_student(self, name, marks):
        add_data = add_stud(self.path, name, marks)
        self.data.append(add_data)
        print("The student has been added successfully")


    def update_mar(self, name, marks):
        updated_data = update_marks(self.path, self.data, name, marks)
        print("Student has been updated successfully")


    def delete_stud(self, name):
        del_data = delete_student(self.path, self.data, name)
        print('Student has been deleted successfully')

    
    def search_stu(self, name):
        found = search_stud(self.data, name)
        if found:
            print("The student has been found successfully")
            return 
        else:
            print("The student not found")


if __name__ == '__main__':
    sm = StudentManager('data/students.txt')   # while executing in terminal, the path should be made into the folder 
    # sm.view_studs()

    sm.add_student('Mani', 88)
    sm.view_studs()