import time
import math


def wrapper(fun):
    def inner(val):
        begin = time.time()
        fun(val)
        end = time.time()
        print(end-begin)
    return inner


@wrapper
def fib(i):
    print(math.factorial(i))


fib(1000)
