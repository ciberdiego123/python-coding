k, n, w = [int(j) for j in input().split()]
s = 0
for i in range(w):
    s += (i+1) * k
if s > n:
    print(str(s-n))
else:
    print('0')
