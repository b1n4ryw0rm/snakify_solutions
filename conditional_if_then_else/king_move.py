x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if (x1 == x2 and abs(y2 - y1) == 1) or (y1 == y2 and abs(x2 - x1) == 1) or (abs(x2 - x1) == 1 and abs(y2 - y1) == 1):
    print("YES")
else:
    print("NO")