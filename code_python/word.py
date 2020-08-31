s = input()
list_s = list(s)
u = 0
lo = 0
for i in list_s:
    if i.islower():
        lo += 1
    else:
        u += 1
if lo >= u:
    s = s.lower()
else:
    s = s.upper()
print(s)



