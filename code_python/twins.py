n = int(input())
coins = list(map(int, input().split()))
coins = sorted(coins)
sum_a = sum(coins)
sum_b = 0
c = 0
while sum_a >= sum_b:
    c += 1
    sum_b += coins[len(coins) - c]
    sum_a -= coins[len(coins) - c]
print(c)
