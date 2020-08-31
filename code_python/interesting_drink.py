n = int(input())
# n = 100000
prices = list(map(int, input().split()))
# prices = []
# for i in range(100000):
#    prices.append(i+1)
prices.sort()
q = int(input())
list_coins_n = []
# Cache to save previous answers
cache = dict()
# Save answers corresponding to given prices
for i in range(1, n):
    if prices[i] != prices[i-1]:
        cache[prices[i-1]] = i

for a in range(q):
    c = int(input())
    if c < prices[0]:
        print(0)
        continue
    if c >= prices[n - 1]:
        print(n)
        continue
    if c in cache:
        print(cache[c])
        continue
    i, j = 0, n - 1
    # Find answer using binary search
    b_m = -1
    while j - i > 0:
        b_m = i + (j - i + 1) // 2
        if b_m == j:
            m = j - 1
        elif b_m == i:
            m = i + 1
        else:
            m = b_m
        if prices[m] > c:
            i, j = i, m
        else:
            i, j = m, j
        if j - i == 1 and prices[i] <= c < prices[j]:
            i, j = i, i
    ans = 0
    if j == 0:
        if c < prices[j]:
            ans = 0
        else:
            ans = 1
    elif i == n - 1:
        if c >= prices[i]:
            ans = n
        else:
            ans = n - 1
    else:
        ans = i + 1
    cache[c] = ans
    print(ans)
