a = int(input())
list = []
while a != 0:
    list.append(a)
    a = int(input())
print(list.index(max(list)) + 1)          