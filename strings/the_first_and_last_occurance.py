s = input()
count = s.count('f')
if count == 1:
    print(s.find('f'))
elif count > 1:
    print(s.find('f'), s.rfind('f'))