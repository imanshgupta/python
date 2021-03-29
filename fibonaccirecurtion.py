def fib(i):
    if i < 0:
        print("invalid input")
    elif i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return fib(i-1)+fib(i-2)


n = int(input("enter no of elements"))
for i in range(n+1):
    print(fib(i))
