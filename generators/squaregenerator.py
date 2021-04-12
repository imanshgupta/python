def sq():
    i = 0
    while True:
        yield i*i
        i = i+1


for i in sq():
    if i > 10:
        break
    print(i)
