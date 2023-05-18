n = int(input())
words = set()

for _ in range(n):
    line = input().split()
    words.update(line)

print(len(words))    
