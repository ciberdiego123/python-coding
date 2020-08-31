n, k = [int(i) for i in input().split()]
T = 240
time_contest = T - k
n_prob = 0
for i in range(n):
    time_contest -= (i+1) * 5
    if time_contest >= 0:
        n_prob += 1
    else:
        break
print(n_prob)

