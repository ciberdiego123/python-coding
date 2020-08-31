def sum_digits(num):
    digits = str(num)
    sum = 0
    n_digits = len(digits)
    for i in range(n_digits):
        sum += int(digits[i])
    return sum


n = int(input())
partitions = [(1, 19), (1000, 100036), (2000, 220033), (3000, 1000027), (4000, 1120024),  (5000, 2000008),
              (6000, 2230003), (7000, 3311020), (8000, 9010000), (9000, 10116100), (10000, 10800100)]
for p in partitions:
    if n >= p[0]:
        k, i = p[0], p[1]
ans = i
if k != n:
    while k < n:
        i += 9
        sum = sum_digits(i)
        if sum == 10:
            ans = i
            k += 1
print(str(ans))
