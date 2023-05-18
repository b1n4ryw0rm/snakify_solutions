n = int(input())
result = {}
for i in range(n):
    words = input().split()
    key = words[0]
    value = words[1:]
    result[key] = value

x = input()

for key, val in result.items():
    if key == x:
        print(*val)
        break
    elif x in val:
        print(key)


# n = int(input())
# d = {}
# for i in range(n):
#     first, second = input().split()
#     d[first] = second
#     d[second] = first
# print(d[input()])