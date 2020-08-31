n = int(input())
f = [0, 0, 0]
for i in range(n):
    x, y, z = [int(j) for j in input().split()]
    f[0] += x
    f[1] += y
    f[2] += z
s = 0
for i in f:
    s += abs(i)
if s == 0:
    print('YES')
else:
    print('NO')
