h = int(input())
m = int(input())
s = int(input())

total_minutes = h * 60 + m + s / 60
hour_angle = 0.5 * ( total_minutes )
print(hour_angle)