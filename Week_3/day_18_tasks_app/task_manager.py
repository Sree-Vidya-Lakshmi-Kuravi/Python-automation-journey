# importing files as modules

from file_handler import *
from utils import *

class TaskManager:

    def __init__(self, path):
        self.path = path
        self.data = get_data(path)
