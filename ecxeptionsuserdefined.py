class Error(Exception):
    """Base class for other exceptions"""
    pass


class ValueTooSmallError(Error):
    """Raised when the input value is too small"""
    pass


class ValueTooLargeError(Error):
    """Raised when the input value is too large"""
    pass


# you need to guess this number
number = 10
while True:
    try:
        i_num = int(input("Enter a number: "))
        if i_num < number:
            raise ValueTooSmallError
        elif i_num > number:
            raise ValueTooLargeError
        break
    except ValueError:
        print("enter an integer")
    except ValueTooSmallError:
        print("This value is too small, try again!")
        print("\n")
    except ValueTooLargeError:
        print("This value is too large, try again!")
        print("\n")

print("Congratulations! You guessed it correctly.")
