a = int(input())
b = int(input())
c = int(input())

x = int(input())
y = int(input())
z = int(input())

current = x * 3600 + y * 60 + z
previous = a * 3600 + b * 60 + c

print(current - previous)