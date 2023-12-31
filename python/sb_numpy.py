import numpy as np
'''

print(x.flags)
print(x.shape)
print(x.strides)
print(x.ndim)
print(x.data)
print(x.size)
print(x.itemsize)
print(x.nbytes)
print(x.base)

print(x.dtype)
print(x.T)
print(x.real)
print(x.imag)
print(x.flat)
for y in x.flat:
    print(y)



print(x.__array_interface__)
print(type(x.__array_struct__))
print(x.ctypes)


print(x.item(3))
print(x.item((1,0)))

print(x.tolist())
print(x.tobytes())
x.tofile('temp.txt', sep='\n', format='%f')
x.tofile('temp.bin', sep='', format='%d')
print('\n')
print(x.dumps())
print('\n')
print(x.astype(np.uint8).dtype)
print(x.astype(np.int16).byteswap(inplace=True))
print(x.view(np.single))
print(x.getfield(np.uint8))
x.setflags(write=False, align=True, uic=False)
print(x.flags)
x.setflags(write=True, align=True, uic=False)
x.fill(1)
print(x)


print(x.reshape((3,2)))
x.resize((5,5))
print(x)

x = np.array([[[0,1],[2,3]],[[4,5],[6,7]]])
print(x.swapaxes(0,2))
print(x.ndim)
print(x.flatten())
print(x.ravel())
x = np.array([[1, 2, 3]], np.int32)
print(x.shape)
print(x.squeeze())



print(x.take((2,3,5)))
x.put((0, 2, 5), (10, 9, 8))
print(x)
print(x.repeat(3))
y = np.array([0]).choose(x)
print(y)

x = np.array([[8, 3475, 2184], [4, 1239, 1056]])
print(x)
x.sort(axis=0)
x.sort()
print(x)

x = np.array([[8, 3475, 2184], [6034, 1239, 1056]])
print(x.argsort(axis=0))
print(x.argsort())
x.partition((1,2))#UHHH

x = np.array([8, 0, 2184])
print(x.searchsorted(203))
print(x.nonzero())
x = np.array([[8, 3475, 2184], [6034, 1239, 1056]])
print(x.compress([1,5,3]))#????????

x = np.array([[5483, 42923, 120938], [8, 3475, 2184], [6034, 1239, 1056]])
print(x.diagonal())


https://numpy.org/doc/stable/reference/arrays.ndarray.html#calculation
'''

