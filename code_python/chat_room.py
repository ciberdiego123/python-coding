word = "hello"
s = input()
i = 0
n = len(word)
for c in s:
    if c == word[i]:
        i += 1
    if i == n:
        break
if i == n:
    print('YES')
else:
    print('NO')

