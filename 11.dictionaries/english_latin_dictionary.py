n = int(input())

latin_english = {}

for _ in range(n):
    english_word, translations = input().split(' - ')
    latin_words = translations.split(', ')
    for latin_word in latin_words:
        if latin_word in latin_english:
            latin_english[latin_word].append(english_word)
        else:
            latin_english[latin_word] = [english_word]

sorted_latin_english = sorted(latin_english.items())

print(len(sorted_latin_english))
for latin_word, translations in sorted_latin_english:
    english_words = sorted(translations)
    print(latin_word + ' - ' + ', '.join(english_words))
