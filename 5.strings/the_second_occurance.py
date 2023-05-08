s = input()
c = s.count('f')
if c == 1:
    print("-1")
elif c < 1:
    print("-2")
else:
    i = s.index('f')
    print(s.index('f', i+1))