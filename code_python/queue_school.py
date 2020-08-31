n, t = [int(i) for i in input().split()]
s = input()
queue = list(s)
for k in range(t):
    i = 0
    while i < n-1:
        if queue[i] == 'B' and queue[i+1] == 'G':
            queue[i], queue[i+1] = queue[i+1], queue[i]
            i += 2
        else:
            i += 1
s = "".join(queue)
print(s)




