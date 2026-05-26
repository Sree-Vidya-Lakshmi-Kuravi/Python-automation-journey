## STRING UTILITY MODULE

def reverse_string(str):
    return str[::-1]


def palindrome_check(str):
    li = list(str)
    left = 0
    right = len(li) - 1
    orig = str

    while left < right:
        li[left], li[right] = li[right], li[left]
        left += 1
        right -= 1
    rev = ''.join(li) 

    return orig == rev


def vowel_count(s):
    count = 0
    for i in s:
        if i in ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']:
            count += 1
    return count

