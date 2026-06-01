# importing files as modules

from file_handler import *
from utils import *

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



    def search_task_id(self, id):
        s = search_data_by_id(self.__data, id)

        if f:
            print(f"Task with id: {id} found")
            view_data(f)

        else:
            print(f"Task with id: {id} not found")


    def update_task_status(self, id):
        try:
            s = search_data_by_id(self.__data, id)

            if s:
                print(f"Select the status choice to update task with id: {id}")
                print("1. Pending")
                print("2. In Progress")
                print("3. Completed")

                ch = input("Enter your choice (1/2/3):")

                if ch == "1":
                    update_status(self.__data, id, 'Pending')

                elif ch == "2":
                    update_status(self.__data, id, 'In Progress')

                elif ch == "3":
                    update_status(self.__data, id, 'Completed')

                else:
                    print("Invalid choice !!")

            else:
                print(f"Task with id: {id} not found")

        except Exception as e:
            print("Some exception occurred !!", e)



    def update_task_priority(self, id):
        try:
            s = search_data_by_id(self.__data, id)

            if s:
                print(f"Select the priority choice to update task with id: {id}")
                print("1. Low")
                print("2. Medium")
                print("3. High")

                ch = input("Enter your choice (1/2/3):")

                if ch == "1":
                    update_prior(self.__data, id, 'Low')

                elif ch == "2":
                    update_prior(self.__data, id, 'Medium')

                elif ch == "3":
                    update_prior(self.__data, id, 'High')

                else:
                    print("Invalid choice !!")

            else:
                print(f"Task with id: {id} not found")

        except Exception as e:
            print("Some exception occurred !!", e)



    def delete_task_by_id(self, id):
        d = delete_by_id(self.__data, id)

        if d:
            print("--------------- Deleted task ---------------")
            view_data(d)
            redefine_id(self.__data)


if __name__ == '__main__':

    path = r'E:\Vidya Career\IT JOB\Repati Kosam\Week_3\day_18_tasks_app\tasks.json'
    tm = TaskManager(path)

