m = []
for i in range(5):
    m.append(list(map(int, input().split())))

for i in range(5):
    for j in range(5):
        if m[i][j] == 1:
            r = abs(i - 2) + abs(j - 2)
print(r)
