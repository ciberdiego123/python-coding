def join_sections(sections):
    j_sections = []
    js = sections.pop(0)
    while len(sections) > 0:
        for s in sections:
            if js[1] < s[0]:
                continue
            elif s[1] < js[0]:
                continue
            else:
                a = min(s[0], js[0])
                b = max(s[1], js[1])
                j_sections.append((a, b))
                sections.remove(s)
    return j_sections


l = int(input())
n = int(input())
painted_sections = []
for i in range(n):
    st, ed = [int(j) for j in input().split()]
    painted_sections.append((st, ed))

joined_sections = join_sections(painted_sections)
painted_sections = sorted(joined_sections, key=lambda section: section[1])
ans = []
if len(painted_sections) == 1:
    print("All painted")
else:
    ans.append(0)
    for s in painted_sections:
        ans.append(s[0])
        ans.append(s[1])
    ans.append(l)
    for i in range(0, len(ans), 2):
        if ans[i] == ans[i+1]:
            continue
        else:
            print(str(ans[i])+" "+str(ans[i+1]))




