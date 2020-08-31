def is_vowel(c):
    vowels = "aeiouy"
    for j in vowels:
        if j == c:
            return True
    return False


s = input()
s = s.lower()
a = ""
for i in s:
    if is_vowel(i):
        continue
    else:
        a += "."+i
print(a)


