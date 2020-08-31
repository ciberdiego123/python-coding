n = int(input())
points = [int(i) for i in input().split()]
a = 0
minp, maxp = points[0], points[0]
for i in range(1,n):
    if points[i] < minp:
        minp = points[i]
        a += 1
    elif points[i] > maxp:
        maxp = points[i]
        a += 1
print(a)
