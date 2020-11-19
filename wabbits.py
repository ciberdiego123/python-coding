cache = dict()


def wabbits(n, k):
    if n == 1 or n == 2:
        return 1
    elif n in cache:
        return cache[n]
    else:
        cache[n] = wabbits(n - 1, k) + wabbits(n - 2, k) * k
        return cache[n]


n, k = [int(i) for i in input().split()]
for i in range(3, n):
    wabbits(i, k)
print(wabbits(n, k))

