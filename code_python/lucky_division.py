n = int(input())
l_num = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777]
b = False
for i in l_num:
    if n % i == 0:
        b = True
        break;
if b:
    print('YES')
else:
    print('NO')
