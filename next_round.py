n, k = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
d = a[k - 1]
if d > 0:
    while k < n and a[k] == d:
        k += 1
else:
    while k - 1 >= 0 and a[k - 1] == 0:
        k -= 1
print(k)
