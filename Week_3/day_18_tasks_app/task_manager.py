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


    


tm = TaskManager(path)
# print(tm.load_tasks())  # list of dictionaries
    
