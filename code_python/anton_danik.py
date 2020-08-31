n = int(input())
games = input()
c = 0
for i in games:
    c += 1 if i == 'A' else -1
ans = 'Anton' if c > 0 else 'Danik' if c < 0 else 'Friendship'
print(ans)
