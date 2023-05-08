m, n = [int(s) for s in input().split()]
a = []
for j in range(m):
    row = input().split()
    for k in range(n):
        row[k] = int(row[k])
    a.append(row)

i, j = [int(s) for s in input().split()]

def swap(a, i, j):
    for row in a:
        row[i], row[j] = row[j], row[i]
    for row in a:    
        print(' '.join([str(elem) for elem in row]))

swap(a, i, j)        