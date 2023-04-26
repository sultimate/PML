# 1.11 展开一个矩阵：将矩阵转换为一维数组

import numpy as np

matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

print(matrix.flatten())
print(matrix.reshape(1, 9))
print(matrix.reshape(1, -1))