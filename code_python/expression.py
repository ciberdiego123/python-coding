a = int(input())
b = int(input())
c = int(input())
if 1 < a and 1 < b and 1 < c:
    ans = a * b * c
else:
    if a == b == c == 1:
        ans = 3
    elif b == 1:
        ans = (min(a, c) + b) * max(a, c)
    elif a == 1:
        ans = a + b
        ans = ans * c if c > 1 else ans + c
    elif c == 1:
        ans = b + c
        ans = ans * a if a > 1 else ans + a
print(ans)
