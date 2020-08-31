n, k = [int(i) for i in input().split()]
m = n // 2 if n % 2 == 0 else n // 2 + 1
if k <= m:
    print(k*2-1)
else:
    k -= m
    print(k * 2)
