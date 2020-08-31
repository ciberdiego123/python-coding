a = input()
b = input()
a = a.lower()
b = b.lower()
if a < b:
    print(str(-1))
elif a == b:
    print(str(0))
else:
    print(str(1))