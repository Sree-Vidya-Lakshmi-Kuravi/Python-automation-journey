
from file_handler import *

def add_task():

    data = get_data(path)

    id = int(input("Enter task id:"))
    title = input("Enter task title:")
    description = input("Enter task description:")
    priority = input("Enter task priority:")

    new_task = {
        "id": id,
        "title": title,
        "description": description,
        "priority": priority,
        "status": "Pending"
    }

    data.append(new_task)

    save_data(path, data)
    print("Data has been added successfully")

# add_task()


def view_tasks():
    data = get_data(path)

    for i in data:
        print("ID:", i['id'], "Title:", i['title'], "||", "Description:", i['description'], '||', "Priority:", i['priority'], '||', "Status:", i['status'])
        print('-------------------------------------------------------------------------------------------------------------------')

# view_tasks()


def search_task_by_title(title):
    data = get_data(path)

    for d in data:
        if d['title'] == title:
            return d

    else:
        print("No such task found")


# print(search_task_by_title("xxx"))


def search_task_by_id(id):
    data = get_data(path)

    for d in data:
        if d['id'] == id:
            return d

    else:
        print("No such task found")

# print(search_task_by_id(12))


def update_task_status_c(id):
    
    data = get_data(path)

    for d in data:
        d['status'] = "Completed"

    return d
    # save_data(path, data)

print(update_task_status_c(10))


def delete_task(id):
    data = get_data(path)
    s = search_task_by_id(id)

    if s != "No such task found":

        if s['id'] == id:
            del s
            
            # save_data(path, data)
            print("Task deleted successfully")
        else:
            print("ID not found")

    else:
        print("No such task found")

# print(delete_task(11))


def filter_task_by_status(status):
    data = get_data(path)
    stat = []

    for i in data:
        if i['status'] == status:
            stat.append(i)
    return stat

# print(filter_task_by_status("Completed"))


def filter_task_by_priority(priority):
    data = get_data(path)
    prior = []

    for i in data:
        if i['priority'] == priority:
            prior.append(i)
    return prior

# print(filter_task_by_priority("High"))


