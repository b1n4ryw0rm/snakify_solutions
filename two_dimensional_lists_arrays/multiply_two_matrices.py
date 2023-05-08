m, n, r = [int(s) for s in input().split()]

a = [[int(s) for s in input().split()] for i in range(m)]
b = [[int(s) for s in input().split()] for i in range(n)]

ab = [[0] * r for i in range(m)]    

for i in range(m):
    for k in range(r):
        for j in range(n):
              ab[i][k] += a[i][j] * b[j][k]

for row in ab:
    print(' '.join([str(elem) for elem in row]))              