'''list1 = ['hellow', "dsdsd", "dsdsdsd", "bye"]
gen = (x[::-1] for x in list1)
print(gen)
for i in list1:
    print(next(gen))
'''
list1 = ['hellow', "dsdsd", "dsdsdsd", "bye"]
gen = (x.upper for x in list1)
print(gen)
for i in list1:
    print(next(gen))
