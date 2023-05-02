n = int(input())
available_sum = 0
total_sum = 0

for i in range(0, n-1):
    a = int(input())
    available_sum += a
for j in range(1, n+1):
    total_sum += j

print(total_sum - available_sum)