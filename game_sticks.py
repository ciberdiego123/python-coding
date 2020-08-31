n, m = [int(i) for i in input().split()]
w = True
while True:
    s = n * m - (n+m-1)
    n -= 1
    m -= 1
    if s > 0:
        w = not w
    else:
        break
if w:
    print('Akshat')
else:
    print('Malvika')
