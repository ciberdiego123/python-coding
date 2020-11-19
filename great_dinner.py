import math

nums = [int(i) for i in input().split()]
n, m = nums[0], nums[1]
for k in range(m):
    d = [int(i) for i in input().split()]

ans = (math.factorial(n) // 2**m) % ((10**9) + 7)
print(ans)
