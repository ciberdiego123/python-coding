n, a, b, c = [int(i) for i in input().split()]
cache = dict()
mini = min(a, b, c)
if n/mini == n//mini:
    cache[n] = n//mini


def cut_ribbon(size):
    if size in cache:
        return cache[size]
    else:
        if size == 0:
            ans = 0
        elif size < 0:
            ans = -40000
        else:
            ans = 1 + max(cut_ribbon(size - a), cut_ribbon(size - b), cut_ribbon(size - c))
        cache[size] = ans
        return ans


cut_ribbon(n//10)
cut_ribbon(n//5)
cut_ribbon(n//4)
cut_ribbon(n//3)
cut_ribbon(n//2)
print(cut_ribbon(n))




