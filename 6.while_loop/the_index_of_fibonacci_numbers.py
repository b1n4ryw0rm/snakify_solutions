a = int(input())

fib1 = 0
fib2 = 1
index = 0

while fib2 < a:
    fib1, fib2 = fib2, fib1 + fib2
    index += 1

if fib2 == a:
    print(index + 1)
else:
    print(-1)    