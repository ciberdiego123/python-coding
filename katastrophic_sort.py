a = input()
b = input()
if a == b:
    print("=")
else:
    n = min(len(a), len(b))
    ans = "="
    num_a, num_b = 0, 0
    for i in range(n):
        if a[i].isnumeric():
            num_a, num_b = int(a[i:]), int(b[i:])
            ans = ">" if num_a > num_b else "<"
            break
        elif a[i] != b[i]:
            ans = ">" if a[i] > b[i] else "<"
            break
    if ans == "=" and len(a) != len(b):
        ans = ">" if len(a) > len(b) else "<"
    print(ans)

