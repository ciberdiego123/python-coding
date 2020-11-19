cache = dict()


def wabbits(n, m):
    if n <= 0:
        return 0, 0
    if n == 1:
        return 1, 1
    if n == 2:
        return 1, 0
    elif n in cache:
        return cache[n]
    else:
        all_rabbits_n1, babies_n1 = wabbits(n - 1, m)
        not_babies_n1 = all_rabbits_n1 - babies_n1
        all_rabbits = all_rabbits_n1 + not_babies_n1 - wabbits(n - m, m)[1]
        babies = not_babies_n1
        cache[n] = (all_rabbits, babies)
        return cache[n]


n, m = [int(i) for i in input().split()]
for i in range(1, n + 1):
    wabbits(i, m)
print(wabbits(n, m)[0])
print(cache)
