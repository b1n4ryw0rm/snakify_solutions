n = int(input())

possible = set(range(1, n+1))
res = possible

while True:
    guess = input()
    if guess == 'HELP':
        break
    guess = {int(x) for x in guess.split()}
    response = input()
    if response == 'YES':
        res &= guess
    else:
        res -= guess
print(" ".join([str(x) for x in sorted(res)]))           