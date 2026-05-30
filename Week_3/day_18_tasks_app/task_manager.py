# importing files as modules

from file_handler import *
from utils import *

path = r'E:\Vidya Career\IT JOB\Repati Kosam\Week_3\day_18_tasks_app\tasks.json'

class TaskManager:

    def __init__(self, path):
        self.path = path
        self.__data = get_data(path)


    def load_tasks(self):
        return self.__data

    
    def save_all_tasks(self):
        save_data(self.path, self.data)

    
    def view_all_tasks(self):
        print("-----------------------------------------------------------------------------------------")

        view_data(self.__data)


    def add_task(self, title, description, priority, status = None):

        t = add_data(self.__data, title, description, priority, status)

        if t:
            self.__data.append(t)


    def filter_by_status(self):
        print("Select the status choice to filter:")
        print('1. Pending')
        print('2. In Progress')
        print('3. Completed')

        try:
            ch = input("Enter your choice(1/2/3):")

            if ch == '1':
                filter_data_by_status(self.__data, "Pending")

            elif ch == '2':
                filter_data_by_status(self.__data, "In Progress")

            elif ch == '3':
                filter_data_by_status(self.__data, "Completed")

            else:
                print("Invalid Choice !!!")

        except Exception as e:
            print("Some exception occurred !!", e)


    def filter_by_priority(self):
        data = self.load_tasks()

        print("Select the priority choice to filter:")
        print("1. Low")
        print("2. Medium")
        print("3. High")

        try:
            ch = input("Enter the choice (1/2/3):")

            if ch == "1":
                filter_data_by_priority(self.__data, "Low")

            elif ch == "2":
                filter_data_by_priority(self.__data, "Medium")

            elif ch == "3":
                filter_data_by_priority(self.__data, "High")

            else:
                print("Invalid choice !!")

        except Exception as e:
            print("Some exception has occurred !!", e)

    


tm = TaskManager(path)

    
