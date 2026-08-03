## Zip two lists

li_1 = [7, 9, 3, 4, 6]
li_2 = [6, 1, 4, 6, 0]

zip_list = zip(li_1, li_2)
# print(list(zip_list)) -> [(7, 6), (9, 1), (3, 4), (4, 6), (6, 0)]
# print(tuple(zip_list)) -> ((7, 6), (9, 1), (3, 4), (4, 6), (6, 0))
# print(dict(zip_list)) -> {7: 6, 9: 1, 3: 4, 4: 6, 6: 0}

for i in zip_list:
    print(i)