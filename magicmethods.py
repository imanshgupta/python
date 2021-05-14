def factorial(x):
    start = 1
    fact = 1
    while start <= x:
        yield fact
        start = start + 1
        fact = fact * start


n = int(input("Enter Number:"))
fact = factorial(n)
for i in fact:
    print(i)
