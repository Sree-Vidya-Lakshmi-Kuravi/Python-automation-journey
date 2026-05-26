def get_stud_data(path):
    with open(path) as f:
        t = f.readlines()
    t1 = []
    for i in t:
        sd = i.split(', ')
        t1.append({'name' : sd[0].strip(), 'marks' : int(sd[1].strip())})
    return t1


def add_data(path, name, marks):
    with open(path, 'a') as f:
        f.write(name+', '+str(marks)+'\n')

    return {'name':name, 'marks':marks}


def update_data(path, d, name, u_marks):
    us = 0
    for i in d:
        if i['name'] == name:
            i['marks'] = u_marks
            us = i
    if us:
        with open(path, 'w') as f:
            for i in d:
                f.write(i['name']+', '+str(i['marks'])+'\n')
        return us
   


def delete_stud(path, d, name):
    ds = []
    for i in d:
        if i['name'] == name:
            d.remove(i)
            ds = i
    with open(path, 'w') as f:
        for i in d:
            f.write(i['name']+', '+str(i['marks'])+'\n')
    return ds


def save_data(path, d):
    with open(path, 'w') as f:
        for i in d:
            f.write(i['name']+', '+str(i['marks'])+'\n')
    return d