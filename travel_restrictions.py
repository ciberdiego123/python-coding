f = open("travel_restrictions_input.txt", "r")
fo = open("travel_restrictions_output.txt", "w")
t = int(f.readline())
for c in range(t):
    n = int(f.readline())
    income = list(f.readline())
    outcome = list(f.readline())
    p = []
    for i in range(n):
        p_country = []
        for j in range(n):
            pij = 'Y' if i == j else '-'
            p_country.append(pij)
        p.append(p_country)
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            else:
                if p[i][j] != '-':
                    continue
                elif outcome[i] == 'N' or income[j] == 'N':
                    p[i][j] = 'N'
                else:
                    p[i][j] = 'Y'
                    if i < j:
                        for tmp in range(i, j):
                            if outcome[tmp] == 'N' or income[tmp+1] == 'N':
                                p[tmp][tmp+1] = 'N'
                                p[i][j] = 'N'
                                break
                    else:
                        for tmp in range(i, j, -1):
                            if outcome[tmp] == 'N' or income[tmp-1] == 'N':
                                p[tmp][tmp-1] = 'N'
                                p[i][j] = 'N'
                                break
    fo.write('Case #')
    fo.write(str(c+1))
    fo.write(':\n')
    for i in range(n):
        line = "".join(p[i])
        fo.write(line)
        fo.write('\n')

