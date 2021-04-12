try:
    n = int(input("enter a number"))
    if n < 10:
        raise numberkamhai("number kam")

except numberkamhai as e:
    print("aour n umber laa0", e.data)
