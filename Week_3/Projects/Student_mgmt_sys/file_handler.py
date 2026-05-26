## VIEW ALL STUDENTS
def get_stud_data(path):

    with open(path) as f:
        t = f.readlines()
    t1 = []

    for i in t:
        w = i.split(',')
        t1.append({'name' : w[0].strip(), 'marks' : int(w[1].strip())})

    return t1


## ADD STUDENT DATA
def add_stud(path, name, marks):

    with open(path, 'a') as f:
        f.write(name + ', ' + str(marks) + '\n')
    
    return {'name':name, 'marks':marks}


## UPDATE THE MARKS
def update_marks(path, d, name, updated_marks):
    d = get_stud_data(path)  # converts the file into list of dictionaries
    us = 0  # stores the updated student

    for i in d:
        if i['name'] == name:
            i['marks'] = updated_marks
            us = i  # stores the updated dictionary

    with open(path, 'w') as f:
        for i in d:
            f.write(i['name'] + ',' + str(i['marks']) + '\n')

    return us 


## DELETE STUDENT
def delete_student(path, d, name):
    d = get_stud_data(path)
    ds = [] # stores the details of student to delete

    for i in d:
        if i['name'] == name:
            d.remove(i)
            ds = i 

    with open(path, 'w') as f:
        for i in d:
            f.write(i['name'] + ',' + str(i['marks']) + '\n')
    
    return ds
