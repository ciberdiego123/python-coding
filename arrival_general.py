def max_min_index(a):
    maxi = 0
    mini = 101
    ans_max = -1
    ans_min = -1
    for i in range(len(a)):
        if maxi < a[i]:
            maxi = a[i]
            ans_max = i
        if mini >= a[i]:
            mini = a[i]
            ans_min = i
    return ans_max, ans_min


n = int(input())
a = [int(i) for i in input().split()]
i, j = max_min_index(a)
di, dj = i, n - j - 1
if j < i:
    print(di+dj-1)
else:
    print(di + dj)
