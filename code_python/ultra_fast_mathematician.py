a = input()
b = input()
c = []
for i in range(len(a)):
    c.append('1' if a[i] != b[i] else '0')
print(''.join(c))
