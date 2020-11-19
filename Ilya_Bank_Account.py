n = int(input())
if n < 0:
    n = abs(n)
    r = n % 100
    n //= 100
    digits = [int(d) for d in list(str(r))]
    if len(digits) == 1:
        digits.append(0)
    mini = min(digits)
    n = -1 * int(str(n) + str(mini))
print(n)
