records = int(input())
a = {}

for i in range(records):
    entry = input().split()
    name = entry[0]
    votes = int(entry[1])
    if name in a:
        a[name] += int(votes)
    else:    
        a[name] = votes

for key, val in sorted(a.items()):
    print(key,val)