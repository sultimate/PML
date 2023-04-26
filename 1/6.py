# 1.6 对矩阵中多个元素，同时执行某个操作

import numpy as np

matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

add_100 = lambda i : i + 100

vectorize_add_100 = np.vectorize(add_100)
print(vectorize_add_100(matrix))