## GET MAXIMUM MARKS
def max_marks(d):
    high = d[0]['marks']

    for i in d:
        if i['marks'] > high:
            high = i['marks']

    return high


## FIND NAME WITH MARKS
def get_name_by_marks(d, m):
    details = []

    for i in d:
        if i['marks'] == m:
            details.append(i)
    return details



## SEARCH STUDENT
def search_stud(d, name):
    for i in d:
        if i['name'] == name.strip():
            return i


## CALCULATE AVERAGE MARKS
def average_marks(d):
    marks_sum = 0
    for i in d:
        marks_sum += i['marks']

    return round(marks_sum/len(d), 2)


## SAVE THE DATA
def save_data(path, d):
    with open(path, 'w') as f:
        for i in d:
            f.write(i['name'] + ',' + str(i['marks']) + '\n') 
    return d