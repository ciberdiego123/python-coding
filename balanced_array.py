t = int(input())
for i in range(t):
    n = int(input())
    if (n // 2) % 2 == 1:
        print('NO')
    else:
        print('YES')
        e, o = 2, 1
        sum_e, sum_o = 0, 0
        results = []
        for j in range(n):
            if j < n // 2:
                results.append(e)
                sum_e += e
                e += 2
            else:
                if j != (n - 1):
                    results.append(o)
                    sum_o += o
                    o += 2
                else:
                    results.append(sum_e - sum_o)
        print(*results)
