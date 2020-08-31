n = int(input())
s = 0
for i in range(n):
    a, b, c = [int(i) for i in input().split()]
    if a+b+c >= 2:
        s += 1
print(s)
