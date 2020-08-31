n, l = [int(i) for i in input().split()]
lanterns = list(map(int, input().split()))
d = 0
lanterns = sorted(lanterns)
distances = []
for i in range(n-1):
    distances.append(lanterns[i+1] - lanterns[i])
distances = list(map(lambda x: x/2, distances))
if lanterns[0] != 0:
    distances.insert(0, lanterns[0])
if lanterns[n-1] != l:
    distances.append(l - lanterns[n-1])
d = max(distances)
print('{0:.10f}'.format(d))
