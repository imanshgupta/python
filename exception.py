'''while True:
    try:
        n = int(input("ENTER A NUMBER"))
        print(n+10)
        break
    except ValueError:
        print("VALUE ERROR is an error where expecting an integer and another data type comes")
    except TypeError:
        print("Type Error is when two diff data types are nade to do apersations ")
    except Exception:
        print("any other")
    except NameError:
        print("name error where we are calling a name that dosnt exists")
    except ZeroDivisionError:
        print("error comes ehn denominator is zero")
    except KeyboardInterrupt:
        print("Interupt happened if press ctrl+c or something else")
    except IndexError:
        print("index error")
    except AttributeError:
        print("attribute not there")
    else:
        print("NO ERROR OCCOURED")
'''
'''

def odd_even(n):
    try:
        assert(n % 2 == 0)
        print()
    except AssertionError:
        print("ASSERTION error for", n)


odd_even(4)
odd_even(3)'''

'''#to check and return an error if a string has all digits or not 
def input(n):
    try:
        assert(n.isdigit())
        print("digit", n)
    except AssertionError:
        print("N IS not  A DIGIT")


input("fdssd")
input("342423423")
'''
a = [1, 2, 3, 4]
try:
    print(a[4])
except IndexError:
    print("index error")
