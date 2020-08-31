import time
a, b = 3, 4
ans = 0
k = 100
while abs(ans - k) > 0.000_000_001:
    # print(a, b)
    m = a + (b - a) / 2
    ans = m ** m
    # print(ans)
    a, b = (a, m) if ans > 100 else (m, b)
print(ans)
print(int(ans))
print(m)
