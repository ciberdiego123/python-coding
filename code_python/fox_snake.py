n, m = [int(i) for i in input().split()]
last = True
for i in range(n):
    s = ''
    for j in range(m):
        if i % 2 == 0:
            s += '#'
        else:
            if (last and j == m - 1) or (not last and j == 0):
                s += '#'
            else:
                s += '.'
    if i % 2 == 1:
        last = not last
    print(s)
