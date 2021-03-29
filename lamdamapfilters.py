"""d=lambda x,y,z:x+y+z
print(d(1,2,3))
----------------------------------

list1 = [1, 2, 3, 4, 5, 6]
list = list(map(lambda x: x*x, list1))
print(list)
# union

list1 = [1, 2, 3, 4, 5, 6]
list2 = [3, 4, 5, 4, 6, 7, 8, 9, 20]
print(list(filter(lambda x: x in list1, list2)))

list1 = ["madam", "mam", "mom", "dad", "sfsffsfs", "dgfdhwew"]


def pal(x):
    if x[::-1] == x:
        return True
    else:
        return False


print(list(filter(pal, list1)))


"""

"""
--------------------------------------
def d(x, y): return x**y
print(d(5, 10))

def con(x, y): return x+y


print(con([56, 7, 676, 867, 6]), [1, 2, 3, 4, 5]))
-----------------------------

list1 = [1, 2, 2, 4]
list2 = [6, 75, 7, 76, 7]
res = list(map(lambda x, y: x+y, list1, list2))
print(res)
--------------------------------

l1 = [12, 3, 24, 243, 53, 64, 7567, 68, 79, 56]
res = list(filter(lambda x: x % 2 == 0, l1))
print(res)
============



l = ["adada", "ad", "dadad", "adada"]
res = list(filter(lambda x: len(x) > 2, l))
print(res)
====================================


#to add 2 lists to 1 will not work as l3[1]...
import math

for i in range(200):
    print(round(math.pi, i))

l1 = [1, 2, 3, 4, 5, 6, 7, 8]
l2 = [1, 2, 3, 4, 5, 6, 7, 8]
l3 = []
for i in range(8):
    print(i)
    l3.append(l1[i]+l2[i])
print(l3)


#to return 2 outputs and to store them
def div(a, b):
    c = a/b
    d = a//b
    return (c, d)


a, b = div(10, 4)
print(a, b)


# to find sum through recursion
def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n-1)


a = sum(1)


a = sum(5)
print(a)


# to take unlimited parameters as input


def sum(*args):
    add = 0
    for i in args:
        add = add+i
    return add


print(sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


def sum(n):
    sum = 0
    for i in range(n*2):
        if(i % 2 == 0):
            sum = sum+i
    return sum


print(sum(5))

for i in "mca":
    print(i, end="")
"""
