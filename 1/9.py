# 1.9 矩阵变形：不改变元素值的前提下，改变一个矩阵的形状（行数和列数）

import numpy as np

# 创建一个4*3的矩阵
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9],
                   [10, 11, 12]])

# 变形 2*6
print(matrix.reshape(2, 6))