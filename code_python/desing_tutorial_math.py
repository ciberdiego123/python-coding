import math


def is_prime(num):
    d = 2
    for i in range(d, int(math.sqrt(num)+1)):
        if num % i == 0:
            return False
    return True


n = int(input())
a = int(math.floor(n/2))
b = int(math.ceil(n/2))
while is_prime(a) or is_prime(b):
    a -= 1
    b += 1
print(a, b)
