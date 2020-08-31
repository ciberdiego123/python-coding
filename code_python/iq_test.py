n = int(input())
x = [int(i) for i in input().split()]
e, o = [], []
for i in range(n):
    if x[i] % 2 == 0:
        e.append(i+1)
    else:
        o.append(i+1)
    if len(o) > 1 and len(e) == 1:
        print(e[0])
        break
    elif len(e) > 1 and len(o) == 1:
        print(o[0])
        break

