n = int(input())
x = [int(i) for i in input().split()]
x.pop(0)
y = [int(i) for i in input().split()]
y.pop(0)
s = set()
for i in x:
    s.add(i)
for i in y:
    s.add(i)
if len(s) == n:
    print('I become the guy.')
else:
    print('Oh, my keyboard!')
