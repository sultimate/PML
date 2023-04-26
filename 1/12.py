# 1.12 计算矩阵的秩（线性代数方法：matrix_rank）

import numpy as np

matrix = np.array([[1, 1, 1],
                   [1, 1, 10],
                   [1, 1, 15]])

print(np.linalg.matrix_rank(matrix)) 