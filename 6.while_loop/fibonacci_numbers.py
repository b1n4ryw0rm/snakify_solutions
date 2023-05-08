n = int(input())
if n <= 1:
    print(n)
else:
    first = 0
    second = 1
    i = 2
    while i <= n:
        fib = first + second
        first = second
        second = fib
        i += 1
        
    print(fib)