import math
t = int(input())
for i in range(t):
    n = input()
    len_n = len(n)
    n = int(n)
    c = 0
    nums = []
    for k in range(len_n):
        d = n % 10
        if d != 0:
            nums.append(int(d*math.pow(10, k)))
            c += 1
        n = n // 10
    print(c)
    print(*nums)

