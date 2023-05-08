s = input()
first = s[:s.find('h') + 1]
last = s[s.rfind('h'):]
middle = s[s.find('h') + 1 : s.rfind('h')]
print(first + middle.replace('h', 'H') + last)