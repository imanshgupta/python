import numpy as np
A = np.arange(1, 6)
print(A)
print(type(A))
print('------------------------------------------')
print(np.median(A))
B = np.array([2, 3, 4, 5, 6])
print(A)
print(B)
print(A+B)
print('------------------------------------------')
print(np.std([1, 2, 2, 3, 4, 5]))
print('------------------------------------------')
print(np.max([1, 2, 2, 11, 4, 5]))
print('------------------------------------------')
print(np.min([1, 2, 2, 11, 4, 5]))
print(' A is as follows')
print(A)
print(' B is as follows')
print(B)
print('sum ofA+ B is as follows')
print(A+B)
print('------------------------------------------')
print(np.identity(2))
print('------------------------------------------')
A2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(A2)
print(A2.shape)
print('------------------------------------------')
A3 = A2.reshape(4, 2)
print(A3)
print('------------------------------------------')
c = np.arange(6)
print(c)
print('------------------------------------------')
print(np.mean(c))
print(np.char.add(['hello'], [' abc']))
print('------------------------------------------')
print(np.char.add(['hello', 'hi'], [' abc', ' xyz']))
a = np.arange(5)
print(a)

#  example of broadcasting
print("bra\oadcasting")
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
b = np.array([2, 2, 3, 4])
print(a)
print(a.shape)

print(b)
print(a+b)

a = np.arange(0, 60, 5)
print(a)
a = a.reshape(3, 4)

print(a)


b = a.T
print(b)


print('Sorted in C-style order:')
c = b.copy(order='C')
print(c)
for x in np.nditer(c):
    print(x, end=' ')


print('Sorted in F-style order:')
c = b.copy(order='F')
print(c)
for x in np.nditer(c):
    print(x, end=' ')

a = np.arange(0, 60, 5)
a = a.reshape(3, 4)

print('Original array is:')
print(a)


print('Modified array is:')

A = np.array([[1, 2, 3, 4],
              [4, 5, 6, 7],
              [5, 6, 2, 10]])
print(A)
print(np.mean(A[0]))
print(np.mean(A[1]))
print(A[0][3])
print(np.median(A[:, 0]))  # median of first column
print(np.median(A[:, 1]))
print(np.median(A[:, 2]))
print(np.median(A[0]))

A = np.arange(1, 6)
print(A)
print('------------------------------------------')
print(A+2)
print('------------------------------------------')
print(A*2)
print('------------------------------------------')
A1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(A1)
A2 = np.array([[1, 1, 1, 1], [5, 6, 7, 8]])
print(A2)
print('------------------------------------------')
print(A1+A2)
