n = int(input())
stones = input()
s = 0
c = 'X'
for i in stones:
    if i == c:
        s += 1
    c = i
print(s)
