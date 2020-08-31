for a in range(1, 10):
    for d in range(0, 10):
        for c in range(0, 10):
            b = 2000 * a - 11000 * d + 112 * c
            if 0 <= b < 10 and int(b) == b and (a+c == d or b+d == c or a+b == c):
                print(a, b, c, d)
                print(str(a+c == d), str(b+d == c), str(a+b == c))


