## File Handling

# Read a file

with open('E:\\Vidya Career\\IT JOB\\Repati Kosam\\Week 1\\Day 07 - File Handling\\sample.txt') as file:
    print(file.read())


# readline() and readlines()

with open('E:\\Vidya Career\\IT JOB\\Repati Kosam\\Week 1\\Day 07 - File Handling\\sample.txt') as file:
    # print(file.read())
    for i in file.readlines():
        print(i.strip())
        

## Write a file

q = ["There is no tomorrow\n", "Hard work beats talent, when talent does not work hard\n", "As above, so below\n", 'The best time is to start now']

# text = "As above, so below"
with open('E:\\Vidya Career\\IT JOB\\Repati Kosam\\Week 1\\Day 07 - File Handling\\sample.txt', 'w') as f:
    f.writelines(q)

# print(write_f())


def write_f1():
    text = "As above, so below"
    with open('E:\Vidya Career\IT JOB\Repati Kosam\Week 1\Day 07 - File Handling\sample11.txt', 'w') as f:
        f.write(text)

# write_f1()


## Appending a file

def append_f1():
    text = "\nThe best time to start is now."
    with open('E:\Vidya Career\IT JOB\Repati Kosam\Week 1\Day 07 - File Handling\sample11.txt', 'a') as f:
        f.write(text)

# append_f1()


## Count words in a file
def c_words():
    with open('E:\\Vidya Career\\IT JOB\\Repati Kosam\\Week 1\\Day 07 - File Handling\\sample.txt') as f:
        t = f.read()
        w = t.split()
        return len(w)
    
# print(c_words())


## Count lines in a file

def count_l():
    with open('E:\\Vidya Career\\IT JOB\\Repati Kosam\\Week 1\\Day 07 - File Handling\\sample.txt') as f:
        t = f.readlines()
        return len(t)

# print(count_l())


## Search word in a file

def search_w(word):
    with open('E:\\Vidya Career\\IT JOB\\Repati Kosam\\Week 1\\Day 07 - File Handling\\sample.txt') as f:
        r = f.read()
        t = r.split()

        if word in t:
            print("The given word exists")
        else:
            print("No such word")

# search_w("luck")


## Copy file contents
def cpy():
    f = open('E:\\Vidya Career\\IT JOB\\Repati Kosam\\Week 1\\Day 07 - File Handling\\sample.txt')
    t = f.read()
    f.close()

    with open("E:\\Vidya Career\\IT JOB\\Repati Kosam\\Week 1\\Day 07 - File Handling\\cpyTxt.txt", "w") as cf:
        cf.write(t)

# cpy()


## Replacing contents in a file

def rep_words():
    with open('E:\\Vidya Career\\IT JOB\\Repati Kosam\\Week 1\\Day 07 - File Handling\\sample.txt', 'r') as f:
        t = f.read()
        t = t.replace('now', 'NOW')
    
    with open('E:\\Vidya Career\\IT JOB\\Repati Kosam\\Week 1\\Day 07 - File Handling\\sample.txt', 'w') as f:
        f.write(t)
        return t
    
rep_words()
