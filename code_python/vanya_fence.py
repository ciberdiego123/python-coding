nh = [int(i) for i in input().split()]
p = [int(i) for i in input().split()]
h = nh[1]
c = 0
for i in p:
    c += 2 if i > h else 1
print(c)
