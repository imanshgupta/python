def wrapperfun(fun):
    def fun2(val):
        print(val)
        fun()
    return fun2


def hellow():
    print("im the sent function inside wrapper")


decorator = wrapperfun(hellow)
decorator(5)
