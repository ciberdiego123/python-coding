import math
n = int(input())
d = math.ceil(n/2)
r = d if n % 2 == 0 else -d
print(r)
