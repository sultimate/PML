# 1.16 计算一个方阵的特征值和特征向量

import numpy as np

matrix = np.array([[1, -1, 3],
                   [1, 1, 6],
                   [3, 8, 9]])

eigenvalues, eigenvectors = np.linalg.eig(matrix)

print(eigenvalues)
print(eigenvectors)