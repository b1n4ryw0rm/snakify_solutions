a = int(input())
count = 0
while a != 0:
    x = a
    a = int(input())
    if a > x:
        count += 1
print(count)