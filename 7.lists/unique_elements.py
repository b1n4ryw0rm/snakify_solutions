a = [int(s) for s in input().split()]
b = []
for elem in a:
    if a.count(elem) == 1:
        b.append(elem)
print(' '.join([str(i) for i in b]))