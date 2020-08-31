a, b = [int(i) for i in input().split()]
a, b = max(a, b), min(a, b)
print(b, (a-b)//2)
