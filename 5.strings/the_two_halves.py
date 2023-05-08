import math
s = input()
length = len(s)
half = math.ceil(length / 2)
print(s[half:] + s[:half])