"""class abc():
    def hi(self):
        print("hi")


a1 = abc()
a1.hi()
# or
print(abc)
print(a1)
# abc.hi()


class defg(abc):
    a2 = abc()
    a2.hi()
"""


class point():
    v1 = 10  # instance of classs

    def f1(self):
        print("hi i am fun f1")

    def f2(self):
        self.f1()


a = point()
print(point.v1)  # class name we can call only attrin=butes
