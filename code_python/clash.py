import calendar as c

m = int(input())
y = int(input())
n = 0
for i in c.Calendar().itermonthdays(y, m):
    if (i != 0): n += 1
print(str(n))
