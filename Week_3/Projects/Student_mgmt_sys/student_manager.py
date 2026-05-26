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
        found = search_stud(self.data, name)
        if not found:
            add_data = add_stud(self.path, name, marks)
            self.data.append(add_data)
            print("The student has been added successfully")
        else:
            print(f"Student with {name} already exists")


    def update_mar(self, name, marks):
        updated_data = update_marks(self.path, self.data, name, marks)
        print("Student has been updated successfully")


    def delete_stud(self, name):
        del_data = delete_student(self.path, self.data, name)

    
    def search_stu(self, name):
        return search_stud(self.data, name)


    def get_topper(self):
        max_m = max_marks(self.data)
        top = get_name_by_marks(self.data, max_m)

        if top:
            if len(top) == 1:
                print("The topper of the class is: ")
                print("Name: ", top[0]['name'])
                print("Marks: ", top[0]['marks'])

            else:
                print("The toppers of the class are: ")

                for i in top:
                    print("-----------------")
                    print("Name: ", i['name'])
                    print("Marks: ", i['marks'])
        else:
            print('No data found !!!!')


    def save_data(self):
        save_data(self.path, self.data)

if __name__ == '__main__':
    sm = StudentManager('data/students.txt')   # while executing in terminal, the path should be made into the folder 
    # sm.view_studs()

    # sm.add_student('Mani', 88)
    sm.search_stu('bvns')
    # sm.view_studs()