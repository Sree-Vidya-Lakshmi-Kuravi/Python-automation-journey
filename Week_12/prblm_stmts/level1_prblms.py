# ===== 1. Frequency Map & Top Element Extractor =====
def most_frequent_element(items: list):
    count = 0
    freq_counter = {}
    top_ele = None
    max_count = 0

    if not items:
        return (None, 0)

    for i in items:
        if i in freq_counter:
            freq_counter[i] += 1
        else:
            freq_counter[i] = 1

    for k, v in freq_counter.items():
        if count > max_count:
            max_count = count
            top_ele = k

    return (top_ele, max_count)

items1 = ["apple", "banana", "apple", "banana", "apple"]
freq_ele1 = most_frequent_element(items1)
# print(freq_ele1)

items2 = [10, 20, 30, 40, 50]
freq_ele2 = most_frequent_element(items2)
# print(freq_ele2)

items3 = []
freq3 = most_frequent_element(items3)
# print(freq3)


# ===== 2. Palindrome Sentence Cleaner & Verifier =====
def is_sentence_palindrome(phrase):
    cleaned_char = ""
    for char in phrase:
        if char.isalnum():
            lower_char = char.lower()
            cleaned_char += lower_char
    if len(cleaned_char) <= 1:
        return True

    left = 0
    right = len(cleaned_char) - 1

    while left < right:
        if cleaned_char[left] != cleaned_char[right]:
            return False
        else:
            left += 1
            right -= 1
    return True

one = is_sentence_palindrome("A man, a plan, a canal: Panama!")
two = is_sentence_palindrome("race a car")
# print(one)
# print(two)


# ===== 3. List Difference & Duplicate Remover =====
def filter_unique_diff(list_a: list, list_b: list):
    res = []
    for i in list_a:
        if i not in list_b and i not in res:
            res.append(i)
    return res

list_1 = [1, 2, 2, 3, 4, 4, 5]
list_2 = [2, 4]

list_3 = [10, 20, 30]
list_4 = [10, 20, 30]

list_5 = [5, 4, 3, 2, 1]
list_6 = []

diff = filter_unique_diff(list_1, list_2)
print(diff)
diff2 = filter_unique_diff(list_3, list_4)
print(diff2)
diff3 = filter_unique_diff(list_5, list_6)
print(diff3)