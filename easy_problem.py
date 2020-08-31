n = int(input())
l = [int(i) for i in input().split()]
if max(l) == 1:
    print('HARD')
else:
    print('EASY')
