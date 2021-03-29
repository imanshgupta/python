import numpy as np
# -------------------------------------------WAYS TO CREATE ARRAY-----------------------------------
a = np.array([1, 2, 3, 4, 5])
print(a)
# to make it explicitely we use dtype=np.int default np.zeros(2) or any pattern makes a float type array of that number
x = np.zeros((5,), dtype=int)
print(x)
intz = np.zeros((2, 4), dtype=int)
print(intz)
ones = np.ones([2, 3], dtype=int)
print(ones)
# there are two more 1 arange and 2 linspace
# in arrange step value is given which gives numbers at a step of that much
# in linspace it returns those many values between the given space
arange = np.arange(10, 50, 10)
print("np.arrange(10,50,10) \n ", arange)
linspace = np.linspace(10, 15, 20)
print("np.linspace(10,15,20) \n", linspace)
# total 3 ways np.array np.arrange np.linspace
# --------------------------------
# ----------------------------INDEXING AND SLICING-------------------------------------------
a = np.arange(10)
b = slice(2, 8, 2)
print(a[b])
a = np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6]])

print('Our array is:')
print(a)

# this returns array of items in the second column
print('The items in the second column are:')
print(a[..., 1])

# Now we will slice all items from the second row
print('The items in the second row are:')
print(a[1, ...])

# Now we will slice all items from column 1 onwards
print('The items column 1 onwards are:')
print(a[..., 1:])
# --------------------------------------BROADCASTING--------------------------------------------------------
