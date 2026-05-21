import Lists

li = [89, 56, 99, 12, 34, 56, 78, 56, 45, 87, 65]

# Storing the list
def storeList(li):
    return li

# Average
def average(li):
    avg = Lists.sum_all(li) / len(li)
    return avg

# Highest mark
high = Lists.max_num(li)

# Lowest mark
low = Lists.min_num(li)

# counting the students who have passed
def count(li):
    count = 0
    for i in li[1:]:
        if i >= 35:
            count += 1
    return count

print("Student Marks: ", storeList(li))
print("Average Mark: ", average(li))
print("Highest Mark: ", high)
print("Lowest Mark: ", low)
print("Number of students passed: ", count(li))
    






