cache_fib = {}


def fib(n):
    if cache_fib.get(n) is not None:
        return cache_fib.get(n)
    else:
        if n < 1:
            v = -1
        elif n == 1:
            v = 0
        elif n == 2:
            v = 1
        else:
            v = fib(n - 1) + fib(n - 2)
        cache_fib[n] = v
        return v


list_n = [10, 50, 100, 200, 500, 1000, 1001, 1002]
for i in list_n:
    print("fib("+str(i)+")="+str(fib(i)))
