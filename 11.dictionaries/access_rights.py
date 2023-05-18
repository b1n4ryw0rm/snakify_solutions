n = int(input())
b = []
c = {'read':'R', 'write':'W', 'execute':'X'}
for i in range(n):
    a = [s for s in input().split()]
    b.append(a)
    # fname = a[0]
    # if a[1] == 'W' or a[2] == 'W' or a[3] == 'W':
    #     wperm = True
    # elif a[1] == 'R' or a[2] == 'R' or a[R] == 'W':
    #     rperm = True
    # elif a[1] == 'X' or a[2] == 'X' or a[3] == 'X':
    #     xperm = True

for row in b:
    print(' '.join(row))   

x = int(input())
d = []
for i in range(x):
    c = [s for s in input().split()]
    d.append(c)