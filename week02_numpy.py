import numpy as np
import random

# v = np.array([1, 3, -9, 2])
# v = np.array([1, 3, -9, 2], dtype='int64')
# v = np.array([
#     [1, 3, -9, 2],
#     [71, 13, -22, 7]]#, dtype='int64')
# print(v.ndim, v.shape, v.data, v.dtype, v.strides)

n = int(input("input number : "))
l = [random.randint(1,100) for i in range(n)]
v = np.array(l, dtype='int16')
print(v)
print(v.ndim, v.shape, v.data, v.dtype, v.strides)