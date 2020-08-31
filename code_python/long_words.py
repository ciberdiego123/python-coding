n = int(input())
for i in range(n):
    line = input()
    l = len(line)
    if l > 10:
        print(line[0]+str(l-2)+line[l-1])
    else:
        print(line)
