n = int(input())
worms = [int(i) for i in input().split()]
k = int(input())
labels = [int(i) for i in input().split()]
for i in range(1, n):
    worms[i] += worms[i - 1]

for c in labels:
    i, j = 0, n - 1
    # Find answer using binary search
    while j - i > 0:
        # Calculate mid_point
        b_m = i + (j - i + 1) // 2
        # Pick first half or second half
        m = j - 1 if b_m == j else i + 1 if b_m == 1 else b_m
        i, j = (i, m) if worms[m] > c else (m, j)
        # Determine the answer when the interval is small enough
        if j - i == 1:
            i, j = (j, j) if worms[i] < c <= worms[j] else (i, i)
    print(str(i+1))
