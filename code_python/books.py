n, t = [int(i) for i in input().split()]
books = list(map(int, input().strip().split(' ')))

ia, ib, m = 0, 0, 0
s = 0
while ib < n:
    i = ib
    while i <= ib:
        if i > n - 1:
            break
        s += books[i]
        if s <= t:
            if (abs(ib - ia) + 1) > m:
                m = abs(ib - ia) + 1
            ib += 1
        i += 1
    s -= books[ia]
    ia += 1
    ib += 1
print(m)