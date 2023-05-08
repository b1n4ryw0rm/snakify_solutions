a = int(input())
max = 0
s_max = 0
while a != 0:
    if a > max:
        s_max = max
        max = a
    elif a > s_max:
        s_max = a    
    a = int(input())
print(s_max)        