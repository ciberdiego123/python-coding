import math
n, m, a = [int(i) for i in input().split()]
d1 = math.ceil(n/a)
d2 = math.ceil(m/a)
print(d1*d2)
