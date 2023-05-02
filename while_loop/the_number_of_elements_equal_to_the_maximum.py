a = int(input())
list = []
while a != 0:
    list.append(a)
    c = list.count(max(list))
    a = int(input())
print(c)        