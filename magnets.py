n = int(input())
m = []
for i in range(n):
    m.append(input())
current = m[0]
c = 1
for i in range(1, n):
    if current != m[i]:
        c += 1
        current = m[i]
print(c)
