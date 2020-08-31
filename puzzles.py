n, m = [int(i) for i in input().split()]
p = [int(i) for i in input().split()]
p.sort()
ans = 1000
for i in range(0, m - n + 1):
    d = p[i + n - 1] - p[i]
    if d < ans:
        ans = d
print(ans)
