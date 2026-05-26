## Dictionaries

# Student Dictionary

x = {
    'name': 'siri',
    'age': 21,
    'marks': 99
}

print(x)

for key, value in x.items():
    print(key, "=>", value)


# Word Frequency Counter

s = "Betty bought a better butter to make the bitter butter better"

def word_freq(s):
    w_list = s.split()
    fd = dict()

    for w in w_list:
        if w in fd:
            fd[w] += 1
        else:
            fd[w] = 1
    
    return fd

print(word_freq(s))


## Merge two dictionaries

x = {
    'name': 'siri',
    'age': 21,
    'marks': 99
}

y = {
    'name1': 'vidya',
    'age1': 19,
    'marks1': 87
}

def merge_dict(x, y):
    return {**x, **y}

print(merge_dict(x, y))


## Find Highest value in Dictionary

d1 = {
    'a': 45,
    'b': 18,
    'c': 7,
    'd': 9
}

# for key, values in d1.items():
#     print(max(d1.values()))
#     break

def max_val(d1):
    m = 0
    k = 0
    for key, value in d1.items():
        if value > m:
            m = value
            k = key
    return k

print(max_val(d1))


# Find character frequency


# Employee Database

emp = [
    {'name': 'siri', 'salary': 90000, 'dept': 'HiTech'},
    {'name': 'mahi', 'salary': 100000, 'dept': 'CS'},
    {'name': 'ram', 'salary': 145000, 'dept': 'QAT'}
]

def pretty_print(emp):
    for i in emp:
        print("Name:", i['name'], "=>", "Salary:", i['salary'], "=>", "Department:", i['dept'])
print(pretty_print(emp))


# Remove Duplicate words

def rem_dup(s):
    d = word_freq(s)
    n = d.keys()
    return ' '.join(n).strip()

print(rem_dup(s))


## Inventory System

store = {'pen': 10, 'books': 5}

def inv_sys(d):
    pens = int(input("Enter the number of pens you want:"))
    books = int(input("Enter the number of books you want:"))

    d['pen'] -= pens
    d['books'] -= books

    return d

print(inv_sys(store))


## Giving the numbers to the words in a sentence

x = "I love python"

def indexed(x):
    s = x.split()
    d = {}
    for i in range(1, len(s)+1):
        d[i] = s[i - 1]

    return d

print(indexed(x))
