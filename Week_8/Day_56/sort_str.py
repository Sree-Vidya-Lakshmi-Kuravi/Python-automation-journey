## Sort strings by length

strs = ['hi', 'hello', 'siri', 'mahi', 'mahidhar', 'sree']

def sort_str_by_len(strs):
    sort_s = sorted(strs, key = len, reverse = True)
    return sort_s

print(sort_str_by_len(strs))