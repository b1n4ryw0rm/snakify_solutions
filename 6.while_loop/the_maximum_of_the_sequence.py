a = int(input())
res = 0
while a != 0:
    if a > res:
        res = a
    a = int(input())
print(res)        