n = int(input())
c = 0
for i in range(n):
    p, q = [int(k) for k in input().split()]
    if q - p >= 2: c += 1
print(c)

