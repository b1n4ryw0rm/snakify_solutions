n, m = [int(s) for s in input().split()]
a, b = set(), set() 
for i in range(n):
    a.add(int(input()))
for j in range(m):
    b.add(int(input()))

print(len(a & b))
print(*sorted(a & b))
print(len(a - (a & b)))
print(*sorted(a - (a & b)))
print(len(b - (a & b)))
print(*sorted(b - (a & b)))