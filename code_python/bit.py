n = int(input())
x = 0
for i in range(n):
    l = input()
    if l.__contains__('+'):
        x += 1
    else:
        x -= 1
print(x)

