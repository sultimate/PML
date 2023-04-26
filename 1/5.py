# 1.5 展示一个矩阵的形状、大小和维数，分别使用 shape.size.ndim 函数

import numpy as np

matrix = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12]])

print(matrix.shape) # (行数，列数)
print(matrix.size)  # 行数*列数
print(matrix.ndim)