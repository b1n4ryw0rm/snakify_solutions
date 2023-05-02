s = input()
first = s[:s.find('h')]
last = s[s.rfind('h') + 1:]
middle = s[s.find('h') : s.rfind('h') + 1]
print(first + middle[::-1] + last)