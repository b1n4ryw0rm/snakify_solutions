n = int(input())
a = []
for i in range(n):
    a.append([])
    for j in range(n):
        if i + j == n - 1:
            a[i].append('1')
        elif j < n - i - 1:
            a[i].append('0')
        else:
            a[i].append('2')       

for row in a:
    print(' '.join(row))