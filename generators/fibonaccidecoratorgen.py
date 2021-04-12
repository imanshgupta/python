import time


def wrapper(fun):
    def fib():
        start = time.time()
        res = fun()
        end = time.time()
        print(end-start)
        return res
    return fib


@wrapper
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b


for i in fib():
    if i > 10:
        break
    print(i)
