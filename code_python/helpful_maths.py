cad = input()
numbers = cad.split('+')
c = [0, 0, 0]
for i in numbers:
    if i == '1':
        c[0] += 1
    elif i == '2':
        c[1] += 1
    else:
        # i == '3'
        c[2] += 1
ans = ""
for i in range(len(c)):
    n = i+1
    for j in range(c[i]):
        ans += str(n)+'+'
ans = ans[0:len(ans)-1]
print(ans)

