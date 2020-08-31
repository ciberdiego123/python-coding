s, n = [int(i) for i in input().split()]
d = []
for k in range(n):
    xi, yi = [int(i) for i in input().split()]
    d.append((xi, yi))
d.sort(key=lambda x: x[0])
i = 0
while i < n:
    if d[i][0] < s:
        s += d[i][1]
    else:
        break
    i += 1
ans = 'YES' if i == n else 'NO'
print(ans)




