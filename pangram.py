n = int(input())
s = input()
if n < 26:
    print('NO')
else:
    s = set(s.lower())
    if len(s) < 26:
        print('NO')
    else:
        print('YES')
