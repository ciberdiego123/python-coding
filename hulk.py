n = int(input())
t = ['I hate', 'I love']
i, s, c, e = 0, '', ' that ', ' it'
while i < n:
    s += t[i % 2]
    i += 1
    s += c if i < n else e
print(s)
