f = open("alchemy_input.txt", "r")
fo = open("alchemy_output.txt", "w")
t = int(f.readline())
for case in range(t):
    n = int(f.readline())
    c = list(f.readline())
    num_a = c.count('A')
    num_b = c.count('B')
    fo.write('Case #')
    fo.write(str(case + 1))
    fo.write(': ')
    if min(num_a, num_b) < (n // 2):
        fo.write('N\n')
    else:
        fo.write('Y\n')


