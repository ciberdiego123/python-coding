n = int(input())
r = dict()
for i in range(n):
    s = input()
    if s in r:
        ns = s + str(r[s])
        print(ns)
        r[ns] = 1
        r[s] = r[s] + 1
    else:
        print('OK')
        r[s] = 1
