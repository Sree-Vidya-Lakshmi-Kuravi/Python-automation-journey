from file_handler import *
from utils import *

class StudentManager:
    def __init__(self, path):
        self.path = path
        self.data = get_stud_data(path)

    def view_studs(self):
        print('--------------------------------------')
        print('Students Data')
        print('--------------------------------------')
        for i in self.data:
            print(i.get('name'), ':', i.get('marks'))

    def get_avg(self):
        avg = average_marks(self.data)
        print("The average marks of all the students is :", avg)

    def add_student(self, name, marks):
        found = search_stud(self.data, name)
        if not found:
            added_data = add_data(self.path, name, marks)
            self.data.append(added_data)
            print("Student Added successfully.")
        else:
            print("Student already exists.")

    def update_marks(self, name, marks):
        found = search_stud(self.data, name)
        if found:
            updated_data = update_data(self.path, self.data, name, marks)
            print("Student updated successfully.")
        else:
            print("Student is not in the data.")

    def delete_stud(self, name):
        found = search_stud(self.data, name)
        if found:
            deleted_data = delete_stud(self.path, self.data, name)
            print("Student deleted successfully")
        else:
            print("Student is not in the data.")
    
    def search_student(self, name):
        found = search_stud(self.data, name)
        if found:
            print("Student found in the data.")
            # print(found)
            return found
        else:
            print("Student not found.")

    def get_topper(self):
        max_marks = get_max_marks(self.data)
        topper = get_name_by_marks(self.data, max_marks)
        if topper:
            if len(topper) == 1:
                print('The topper of the class is :')
                print('Name :', topper[0]['name'])
                print('Marks :', topper[0]['marks'])
            else:
                print("The toppers of the class are : ")
                for i in topper:
                    print('----------------------')
                    print('Name :', i['name'])
                    print('Marks :', i['marks'])
        else:
            print('No data found !!!')

    def save_data(self):
        save_data(self.path, self.data)


if __name__ == '__main__':

    sm = StudentManager('data/students.txt')
    # sm.view_studs()
    # sm.delete_stud('ram')
    # sm.view_studs()
    sm.add_student('ram', 98)
    # sm.view_studs()
    # sm.update_marks('ram', 100)
    # sm.view_studs()
    # sm.search_student('ram')
