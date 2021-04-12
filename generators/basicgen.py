def gen(val):
    i = 0
    while i < val:
        yield i+1
        i = i+1


'''
for i in gen(5):
    print(i)
'''
x = gen(5)
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
