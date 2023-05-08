def capitalize(lower_case_word):
    cap_letter = chr(ord(lower_case_word[0]) - 32)
    return cap_letter + lower_case_word[1:]

source = input().split()
res = []
for word in source:
    res.append(capitalize(word))
print(' '.join(res))    