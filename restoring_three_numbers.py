x = [int(i) for i in input().split()]
m = max(x)
results = list(map(lambda d: m - d, x))
results.remove(0)
print(*results)
