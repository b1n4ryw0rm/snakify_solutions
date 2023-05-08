a = [int(s) for s in input().split()]
mx = a.index(max(a))
mn = a.index(min(a))
a[mx], a[mn] = min(a), max(a)
print(' '.join([str(i) for i in a]))