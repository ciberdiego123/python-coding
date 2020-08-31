n = int(input())
max = 0
c = 0
for i in range(n):
    a, b = [int(i) for i in input().split()]
    c -= a
    c += b
    if max < c:
        max = c
print(max)
