n, m = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
t, c = 0, 0
for i in range(m):
    va = a[i] - 1
    if c <= va:
        t += va - c
    else:
        t += va + n - c
    c = va
print(t)
