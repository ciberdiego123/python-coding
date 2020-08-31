t = int(input())
for i in range(t):
    n = int(input())
    r = n // 2 if n % 2 == 1 else n // 2 - 1
    print(r)
