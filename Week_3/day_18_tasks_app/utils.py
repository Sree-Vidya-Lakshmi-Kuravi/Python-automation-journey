
class TaskTitleEmptyError(Exception):
    pass

class TaskStatusError(Exception):
    pass

class TaskPriorityError(Exception):
    pass


def add_data(data, title, description, priority, status):

    if not status:
        status = "Pending"

    try:
        if title == "":
            raise TaskTitleEmptyError

        if priority not in ("Low", "High", "Medium"):
            raise TaskPriorityError

        if status not in ("Pending", "In Progress", "Completed"):
            raise TaskStatusError

        if title != "" and priority in ("Low", "Medium", "High") and status in ("Pending", "In Progress", "Completed"):
            data = data.copy()

            new_task = {
                "id": id,
                "title": title,
                "description": description,
                "priority": priority,
                "status": "Pending"
            }

            return new_task

    except TaskTitleEmptyError:
        print("Task title must not be empty")
    
    except TaskPriorityError:
        print("Task priority must be Low/Medium/High")

    except TaskStatusError:
        print("Task status must be Pending/In Progress/Completed")

    except Exception as e:
        print("Some exception has been occurred!!", e)



def view_data(data):
    data = data.copy()

    try:
        for i in data:
            print("ID:", i['id'])
            print("Title:", i['title'])
            print("Description:", i['description'])
            print('Priority:', i['priority'])
            print('Status:', i['status'])
            print('-------------------------------------------------------------------------------------------------------------------')

    except Exception as e:
        print("Some Exception occurred in view_data !!", e)



def search_data_by_id(data, id):
    data = data.copy()
    found = []

    try:
        for d in data:
            if d.get('id') == id:
                found.append(d)
                break
        return found

    except Exception as e:
        print('Some exception occurred in search_data_by_id!!', e)



def search_data_by_title(data, title):
    data = data.copy()
    found = []

    try:
        for d in data:
            if d.get('title') == title:
                found.append(d)
                break
        return found

    except Exception as e:
        print('Some exception occurred in search_data_by_title!!', e)



def filter_data_by_status(data, status):
    data = data.copy()
    stat = []

    try:
        for i in data:
            if i.get('status') == status:
                stat.append(i)
        view_data(stat)
        return stat

    except Exception as e:
        print("Some exception occurred in filter_data_by_status!!", e)



def filter_data_by_priority(data, priority):
    data = data.copy()
    prior = []

    try:
        for i in data:
            if i.get('status') == status:
                prior.append(i)
        view_data(prior)
        return prior

    except Exception as e:
        print("Some exception occurred in filter_data_by_priority!!", e)


def update_status(data, id, status):
    try:
        for d in data:
            if d.get('id') == id:
                d['status'] = status
                print("Task has been updated successfully !!")
                break

    except Exception as e:
        print("Some exception occurred in update_status !!", e)


def update_prior(data, id, priority):
    try:
        for d in data:
            if d.get('id') == id:
                d['priority'] = priority
                print("Task has been updated successfully !!")
                break
    except Exception as e:
        print("Some exception occurred in update_prior !!", e)



def delete_by_id(data, id):
    try:
        deleted = []
        for d in data:
            if d.get('id') == id:
                deleted.append(d)
                data.remove(d)
                break
        else:
            print(f"Task with id: {id} is not found")
        return deleted

    except Exception as e:
        print("Some exception occurred in delete_by_id !!")


def  redefine_id(data):
    for d in range(len(data)):
        data[d]['id'] += 1
    
