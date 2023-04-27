# 1.14 获取矩阵的对角线元素

import numpy as np

matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

print(matrix.diagonal())
print(matrix.diagonal(offset=1))
print(matrix.diagonal(offset=-1))