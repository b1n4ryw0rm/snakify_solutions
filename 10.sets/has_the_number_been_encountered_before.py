a = set()
for num in input().split():
    if num in a:
        print('YES')
    else:
        print('NO')
        a.add(num)