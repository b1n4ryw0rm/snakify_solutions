n = int(input())
word_count = {}
for i in range(n):
    words = input().split()
    for i, word in enumerate(words):
        count = word_count.get(word, 0)
        word_count[word] = count + 1

max_value = max(word_count.values())

tot_max_keys = []
for key, val in word_count.items():
    if val == max_value:
        tot_max_keys.append(key)

max_keys_sorted = sorted(tot_max_keys)
print(max_keys_sorted[0])