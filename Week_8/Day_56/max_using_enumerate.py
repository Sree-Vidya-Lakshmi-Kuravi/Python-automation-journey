## Find max element using enumerate()
# The enumerate() function in Python is used to iterate over an iterable while keeping track of both the index and the value. 
# It returns pairs in the form (index, element). 


num = [9, 5, 3, 5, 6, 2]

def max_enum(num):
    i, e = max(enumerate(num), key = lambda x:x[1])
    print(i, e)

max_enum(num)


max_ele = num[0]
lar_i = 0

for i,e in enumerate(num, start=1):
    if e > max_ele:
        lar_i = i
        max_ele = e
print(lar_i)
print(max_ele)