n = int(input())
money = list(map(int, input().split()))
max_c = 0
i = 0
while i < n:
    maxi = 0
    c = 0
    while i < n and money[i] >= maxi:
        maxi = money[i]
        c += 1
        i += 1
    if c > max_c:
        max_c = c
print(max_c)
