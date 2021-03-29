while True:
    print("1-to get last item of list")
    print("2-to add an item to list")
    print("3-to remove an item from last of the list")
    print("4-to sort the list in increasing order")
    print("5-to concatenate two lists")
    print("6-to slice the list")
    print("7-to remove an element at specific location")
    print("8-to fetch any index element of list")
    print("9-to get the length of list")
    print("10-to get the minimum value")
    print("11- to get the maximum value")
    print("12-to check whether item is present in list or not")
    print("0-Exit")
    ch = int(input("enter your choice"))
    l = list()
    l1 = list()
    if(not ch):
        print("wrong choice entered")
    else:
        if(ch == 1):
            for i in range(5):
                i = input("enter a number")
                l.append(i)
            print(l[-1])
        elif (ch == 2):
            val = input("enter an item to be appended")
            l.append(val)
        elif(ch == 3):
            l.pop()
        elif(ch == 4):
            l = l.sort()
            print(l)
        elif(ch == 5):
            for i in range(5):
                i = input("enter a number")
                l1.append(i)
            print(l.extends(l1))
        elif(ch == 6):
            print(l[2, 4])
        elif(ch == 7):
            loc = int(input("enter the location"))
            if((len(l)) < loc):
                l.pop(loc)
            else:
                print("location not available")
            print(l)
        elif(ch == 0):
            break

        else:
            print("Wrong choice entered")
