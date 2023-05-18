word_counts = {}

words = input().split()

for i, word in enumerate(words):
    count = word_counts.get(word, 0)
    
    print(count, end=' ')
    
    word_counts[word] = count + 1