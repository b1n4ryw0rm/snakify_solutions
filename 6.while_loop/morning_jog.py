a = int(input())
b = int(input())
days = 1
while a < b:
    a = a + (a * (10 / 100))
    days += 1
print(days)    