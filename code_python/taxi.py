n = int(input())
children = list(map(int, input().split()))
c = 0
taxi = 0
count_list = [0, 0, 0, 0, 0]
for i in range(5):
    count_list[i] = children.count(i)

c += count_list[4]
count_list[4] = 0
if count_list[3] > 0:
    if count_list[1] > 0:
        if count_list[1] >= count_list[3]:
            c += count_list[3]
            count_list[1] -= count_list[3]
            count_list[3] = 0

        else:
            c += count_list[1]
            count_list[3] -= count_list[1]
            count_list[1] = 0
    else:
        c += count_list[3]
        count_list[3] = 0

c += count_list[3]
count_list[3] = 0

c += count_list[2] // 2
count_list[2] = count_list[2] % 2

c += count_list[1] // 4
count_list[1] = count_list[1] % 4

if count_list[2] == 1 and count_list[1] == 3:
    c += 2
elif count_list[2] == 0 and count_list[1] == 0:
    c += 0
else:
    c += 1
count_list[2] = 0
count_list[1] = 0

print(c)



