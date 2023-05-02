n = int(input())
a = n
len = 1
lst = []
while n != 0:
    n = int(input())
    if n == a:
        len += 1
    else:
        a = n
        len = 1
    lst.append(len)
print(max(lst))