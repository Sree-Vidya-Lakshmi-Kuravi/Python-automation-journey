## Sort students by marks

def sort_stu(s_marks: list):
    if len(s_marks) == 0:
        print("Student marks list is empty")
    elif len(s_marks) == 1:
        return s_marks
    else:
        s_marks.sort()
        return s_marks

s_marks = [89, 76, 23, 56, 90]
print(sort_stu(s_marks))