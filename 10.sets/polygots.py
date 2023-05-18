n = int(input())  
languages = []  

for _ in range(n):
    num_languages = int(input())  
    student_languages = set()  
    
    for _ in range(num_languages):
        language = input()
        student_languages.add(language)

    languages.append(student_languages)  


common_languages = set.intersection(*languages)
num_common_languages = len(common_languages)


all_languages = set.union(*languages)
num_all_languages = len(all_languages)


print(num_common_languages)
print(*sorted(common_languages), sep="\n")
print(num_all_languages)
print(*sorted(all_languages), sep="\n")
