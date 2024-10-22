import numpy as np
np1 = np.array([1,2,3,4,5,6])
print(np1[:3])
np2 = np.full((2,8), 7)
print(np2)
np3 = np.full((6, 6), 6)
print(np3.shape)
np4 = np.zeros((3,6), dtype='int64')
np4[0,3] = 40
np4[1, 3] = 50
np4[2,3] = 60
print(np4)
np5 = 12*np.ones((3,3))
print(np5)
# If the dimension is one it is called as vector
# If the dimension is two it is called as matrix
# If the dimension is three it is called Tensor
