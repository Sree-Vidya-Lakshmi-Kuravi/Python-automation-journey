def search_stud(d, name):
    for i in d:
        if i['name'] == name.strip():
            return i
        

def average_marks(d):
    s = 0
    for i in d:
        s += i['marks']
    return round(s / len(d), 2)


def get_name_by_marks(d, m):
    ms = []
    for i in d:
        if i['marks'] == m:
            ms.append(i)
    return ms


def get_max_marks(d):
    m = d[0]['marks']
    for i in d:
        if i['marks'] > m:
            m = i['marks']
    return m
