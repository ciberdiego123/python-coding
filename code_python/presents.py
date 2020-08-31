n = int(input())
p = list(map(int, input().split()))
p.insert(0, 0)
L = [0]
for i in range(1, n+1):
    L.append(p.index(i))
print(*L[1:n+1])

