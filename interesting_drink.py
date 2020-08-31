n = int(input())
prices = list(map(int, input().split()))
prices.sort()
q = int(input())
list_coins_n = []
# Cache to save previous answers
cache = dict()
if n >= 50000:
    # Divide the prices list
    for i in range(1000):
        list_coins_n.append((prices[i * n // 1000], i * n // 1000))
    list_coins_n.append((prices[n - 1], n - 1))
if n >= 1000:
    for i in range(100):
        list_coins_n.append((prices[i * n // 100], i * n // 100))
    list_coins_n.append((prices[n - 1], n - 1))

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
    # Get interval to find the answer
    for b in range(len(list_coins_n) - 1):
        if c >= list_coins_n[b][0]:
            i, j = list_coins_n[b][1], list_coins_n[b + 1][1]
        else:
            break
    # Find answer using binary search
    b_m = -1
    while j - i > 0:
        if b_m == j:
            m = j - 1
        elif b_m == i:
            m = i + 1
        else:
            m = i + (j - i + 1) // 2
        if prices[m] > c:
            i, j = i, m
        else:
            i, j = m, j
        if j - i == 1 and prices[i] <= c < prices[j]:
            i, j = i, i
        b_m = m
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