a = int(input())
b = int(input())
n = int(input())

total_cost = (a * 100 + b) * n
dollars = total_cost // 100
cents = total_cost % 100

print(dollars, cents)