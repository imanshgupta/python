def sum(a, b, c):
    return a+b+c


def work(fun):
    result = fun(3, 4, 5)
    return result


print(work(sum))
