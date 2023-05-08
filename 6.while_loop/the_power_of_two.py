n = int(input())
x = 0
while pow(2, x) <= n:
    exp = x
    res = pow(2, x)
    x += 1
print(exp, res)    