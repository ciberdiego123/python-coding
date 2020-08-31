g = list(input())
r = list(input())
p = list(input())
gr = []
gr.extend(g)
gr.extend(r)
gr.sort()
p.sort()
if gr == p:
    print('YES')
else:
    print('NO')