# 1.19 矩阵运算-相乘

import numpy as np

matrix_a = np.array([[1, 1],
                     [1, 2]])

matrix_b = np.array([[1, 3],
                     [1, 2]])

# 矩阵相乘
print(np.dot(matrix_a, matrix_b))
print(matrix_a @ matrix_b)

# 矩阵对应元素相乘
print(matrix_a * matrix_b)