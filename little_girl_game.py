import string
# import time
s = input()
letters = string.ascii_lowercase
count = dict()
for i in letters:
    count[i] = 0
for i in s:
    count[i] = count[i] + 1
n = len(s)
count_values = list(filter(lambda x: x > 0, count.values()))
n_count = len(count_values)
w = True
while True:
    n_even = len(list(filter(lambda x: x % 2 == 0, count_values)))
    n_odd = n_count - n_even
    changed = False
    # print(n, n_count, n_even, n_odd)
    # print(count_values)
    # time.sleep(1)
    if n % 2 == 0 and n_even == n_count:
        break
    if n % 2 == 1 and n_odd == 1:
        break
    if n % 2 == 1 or (n % 2 == 0 and n_odd > 1):
        for i in range(n_count):
            if count_values[i] % 2 == 0 and count_values[i] > 0:
                count_values[i] = count_values[i] - 1
                changed = True
                break
    if not changed:
        for i in range(n_count):
            if count_values[i] > 0:
                count_values[i] = count_values[i] - 1
                changed = True
                break
    n -= 1
    w = not w
ans = 'First' if w else 'Second'
print(ans)





