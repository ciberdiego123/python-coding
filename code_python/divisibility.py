import math
t = int(input())
for i in range(t):
    a, b = [int(k) for k in input().split()]
    if a <= b:
        print(b - a)
    else:
        print((math.ceil(a/b) * b)-a)
