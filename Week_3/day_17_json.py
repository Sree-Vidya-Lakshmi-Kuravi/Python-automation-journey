## JSON HANDLING

import json

data = [
    {"id": 1, "name": "siri", "marks": 85},
    {"id": 2, "name": "mahi", "marks": 90},
    {"id": 3, "name": "ram", "marks": 78},
    {"id": 4, "name": "vijay", "marks": 92},
    {"id": 5, "name": "pradeep", "marks": 88},
]
path = r'E:\Vidya Career\IT JOB\Repati Kosam\students.json'

# storing the data
def get_data(path):
    with open(path) as file:
        f = json.load(file)
        return f

## Adding the data
def add_data(path):
    with open(path, 'w') as f:
        json.dump(data, f, indent = 4)

add_data(path)


## Printing the data
def print_data(path):
    with open(path, 'r') as f:
        file = json.load(f)
        for i in file:
            print("Id:", i['id'], '||', "Name:", i['name'], '||', "Marks:", i['marks'])

# print_data(path)


# adding the student
def add_stu(path, id, name, marks):
    students = get_data(path)
    stu = {'id': id, 'name': name, 'marks': marks}
    students.append(stu)

    with open(path, 'a') as f:
        json.dump(students, f, indent = 4)

# add_stu(path, 6, "bvns", 88)


# search student by name
def search_by_name(path, name):
    students = get_data(path)
    for i in students:
        if i.get("name") == name:
            return i

# print(search_by_name(path, "pradeep"))


# converting dictionary to json
def dict_to_json(path):
    students = get_data(path)
    string = json.dumps(students)
    return string

print(dict_to_json(path))