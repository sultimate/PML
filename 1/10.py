# 1.10 转置向量或矩阵

import numpy as np

matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

print(matrix.T)

vector_row = np.array([1, 2, 3]) # 所以一个向量是不能转置的（或者说无效的）
print(vector_row.T)

matrix_row = np.array([[1, 2, 3]])
print(matrix_row.T)

matrix_column = np.array([[1],
                          [2],
                          [3]])
print(matrix_column.T)