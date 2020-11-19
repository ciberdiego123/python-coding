import sys

n = int(input())
ans, r = -1, 1
stack_ans = []
last_level = 2**(n - 1)
while ans != 0:
    print(r)
    sys.stdout.flush()
    ans = int(input())
    if ans == 0:
        print(f'! {r}')
        break
    if ans == 2 and r >= last_level:
        print(f'! {r+1}')
        break
    if len(stack_ans) > 0:
        prev_ans = stack_ans[len(stack_ans)-1]
        if prev_ans < ans:
            if prev_ans == 1:
                r += 1
            else:
                r = (r + 1) * 2
                stack_ans.append(ans)
                stack_ans.append(ans-2)
                continue
        else:
            r *= 2
    else:
        r *= 2
    stack_ans.append(ans)

