import json

path = r'E:\Vidya Career\IT JOB\Repati Kosam\Week_3\day_18_tasks_app\tasks.json'

# get data
def get_data(path):
    try:
        with open(path) as file:
            tasks = json.load(file)
            return tasks
    except FileNotFoundError:
        print("No such file found")

# print(get_data(path))


# save data
def save_data(path, data):
    try:
        pass
    except Exception as e:
        print('Some exception has occurred')

