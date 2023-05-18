n = int(input())
text = [input().split() for _ in range(n)]

word_counts = {}

for line in text:
    for word in line:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

sorted_words = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))

for word, count in sorted_words:
    print(word)
