m, n = [int(s) for s in input().split()]
a = []
for j in range(m):
    row = input().split()
    for k in range(n):
        row[k] = int(row[k])
    a.append(row)

c = int(input())

for row in a:
    print(' '.join([str(elem * c) for elem in row]))