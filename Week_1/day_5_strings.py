# ## Count Vowels
# def count_vowels(string : str):
#     count = 0
#     for i in string:
#         if i in 'aeiou' or i in 'AEIOU':
#             count += 1
#     return count
# print(count_vowels("vidyalakshmi"))
# print(count_vowels("fantastic four"))
# print(count_vowels("mahikaduihi"))


# ## Reverse a string without [::-1]
# def revStr(string : str):
#     li = list(string)
#     left = 0
#     right = len(li) - 1

#     while left < right:
#         li[left], li[right] = li[right], li[left]
#         left += 1
#         right -= 1
#     return ''.join(li)

# print(revStr('siri'))


# ## Check Palindrome
# def is_palindrome(string : str):
#     li = list(string)
#     left = 0
#     right = len(li) - 1
#     orig = string

#     while left < right:
#         li[left], li[right] = li[right], li[left]
#         left += 1
#         right -= 1
#     rev = ''.join(li) 

#     return orig == rev

# print(is_palindrome('amma'))
# print(is_palindrome('ammmaaaaawwww'))


# ## Count words in a sentence

# sen = "Mahi Ram BVNS Kuravi Sree Vidya Lakshmi"

# def words_in_sen(sen):
#     # count = 0
#     # s = sen.split(" ")
#     # for i in s:
#     #     count += 1
#     # return count
#     return len(sen.split(" "))

# print(words_in_sen(sen))


## Find Character Frequency

# def char_freq(string : str):
#     d = {}
#     for i in string:
#         if i in d:
#             d[i] += 1
#         else:
#             d[i] = 1

#     for i in d:
#         print(i, "=", d[i])
#     return d

# print(char_freq("rohitsharma"))


# ## Remove spaces from string

# s = "Mahi Ram BVNS Kuravi Sree Vidya Lakshmi"

# def rem_spaces(s : str):
#     x = s.split(" ")
#     return ''.join(x)
#     #return s.replace(" ", "")

# print(rem_spaces(s))


# ## Longest word in a sentence

# s = "Mahi Ram BVNS Kuravi Sree Vidya Lakshmi"

# def longest(s : str):
#     long_w = ''
#     for i in s.split():
#         if len(i) > len(long_w):
#             long_w = i
#     return long_w

# print(longest(s))



# # Capitalize first letter of each word
# s = "mahi ram bVNS kuravi sree vidya lakshmi"

# def cap_first(s : str):

#     # x = s.split(" ")
#     # for i in x:
#     #     z = i.capitalize()
#     #     print(z, end = " ")

#     return " ".join(i.capitalize() for i in s.split(" "))

# print(cap_first(s))


## Replace vowels with numbers
# s = "siri"
# x = ['a', 'e', 'i', 'o', 'u']
# res = ""
# def rep_v_n(s):
#     for i in s:
#         if i.lower() in x:
#             res = i.replace("['a', 'e', 'i', 'o', 'u']", "[1, 2, 3, 4, 5]")
#     return res

# print(rep_v_n(s))


s = "siri"
res = ""

vow = {
    'a': '1',
    'e': '2',
    'i': '3',
    'o': '4',
    'u': '5'
}

for i in s:
    if i.lower() in vow:
        res += vow[i.lower()]
        print(res)
    else:
        res += i
        print("Resu: ", res)
    








