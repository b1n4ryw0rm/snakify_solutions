n = int(input())
a = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(abs(i-j))
    a.append(row)
for row in a:
    print(' '.join([str(elem) for elem in row]))