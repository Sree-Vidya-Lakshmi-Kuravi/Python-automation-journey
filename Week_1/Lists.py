# ## Find Maximum Number
li = [1, 23, 34, 8, 23]


def max_num(li):
    max_num = li[0]

    # for i in range(1, len(li)):
    #     if li[i] > max_num:
    #         max_num = i

    for i in li[1:]:  # starts comparing from second element
        if i > max_num:
            max_num = i
    print("Maximum Number: ")
    return max_num


## Find Minimum Number
def min_num(li):
    min_num = li[0]

    for i in li[1:]:
        if i < min_num:
            min_num = i
    print("Minimum Number: ")
    return min_num


# ## Sum of all elements
def sum_all(li):
    total = 0

    for i in li:
        total += i
    print("Total Sum: ")
    return total

print(sum_all(li))


## Count Even and Odd Numbers in a List
def count_even_odd(li):
    odd_c = 0
    even_c = 0
    for i in li:
        if i % 2 == 1:
            odd_c += 1
        elif i % 2 == 0:
            even_c += 1

    return odd_c, even_c
print(count_even_odd(li))

## Reverse a List

# rev_li = []
# for i in li[::-1]:
#     rev_li.append(i)
# print("Reversed List: ", rev_li)

def reverse_list(li):
    n = len(li)
    left = 0
    right = n-1

    while left < right:
        li[left], li[right] = li[right], li[left]
        left += 1
        right -= 1
    return li

print(reverse_list(li))


## Remove Duplicates
def remove_dup(li):
    li1 = []
    for i in li:
        if i not in li1:
            li1.append(i)
        else:
            continue
    print("Clean List: ")
    return li1
print(remove_dup(li))


## Find Second Largest Number
def second_largest(li):
    largest = li[0]
    sec_largest = li[0]

    for i in li:
        if i > largest:   
            sec_largest = largest
            largest = i
        elif i > sec_largest:
            sec_largest = i
        else:
            continue
    print("Second Largest Number: ")
    return sec_largest

print(second_largest(li))


## Sort List without sort()
def sorting(li):
    print("List before sorting:")
    print(li)

    for i in range(len(li)):
        print("----------------------")
        for j in range(i + 1, len(li)):
            print(i, j)
            if li[i] > li[j]:
                li[i], li[j] = li[j], li[i]
                print(li)
    print("List after sorting:")
    return li

print(sorting(li))
