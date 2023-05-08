a = [int(s) for s in input().split()]
flag = 0
for i in range(1,len(a)):
  if (a[i] > 0 and a[i-1] > 0) or (a[i]<0 and a[i-1]<0):
    flag = 1
    break
if flag == 1:
    print(a[i-1],a[i])