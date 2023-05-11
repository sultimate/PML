# 1.15 计算矩阵的迹 trace: 即对角线元素之和

import numpy as np

matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

print(matrix.trace())
print(np.sum(matrix.diagonal()))