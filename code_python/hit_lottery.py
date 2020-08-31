n = int(input())
m = [100, 20, 10, 5, 1]
s = 0
for i in m:
    r = n // i
    n = n % i
    s += r
print(s)
