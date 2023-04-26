# 1.3 创建一个稀疏矩阵

import numpy as np
from scipy import sparse

matrix = np.array([[0, 0],
                   [0, 1],
                   [3, 0]])

# 创建一个压缩的稀疏行（Compressed Sparse Row, CSR）矩阵
matrix_sparse = sparse.csr_matrix(matrix)
print(matrix)
print(matrix_sparse)

matrix_large = np.array([[0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 1, 0, 0, 0, 0, 0, 0],
                         [3, 0, 0, 0, 0, 0, 0, 0]])
matrix_large_sparse = sparse.csr_matrix(matrix_large)
print(matrix_large_sparse)