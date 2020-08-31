import math

t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    c_dict = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: [], 11: []}
    c_list = []
    m = 0
    if n <= 11:
        m = n
        for k in range(m):
            c_list.append(k+1)
    else:
        while len(c_list) < n:
            for k in range(m):
                d = k+1
                if len(c_dict[d]) == 0:
                    c_dict[d].append(l[len(c_list)])
                    c_list.append(d)
                    break

    print(m)
    print(*c_list)


